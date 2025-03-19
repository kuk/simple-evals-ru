
import os
import json
import asyncio
import logging
import time
import argparse
import random
from pathlib import Path
from functools import partial

from simple import registry

from simple.clients.openrouter import OpenrouterClient
from simple.clients.yandexgpt import YandexgptClient
from simple.clients.gigachat import GigachatClient
from simple.clients.runpod import RunpodClient
from simple.clients.e2b import E2BClient

from simple.benches.bbh import bbh_worker
from simple.benches.humaneval import humaneval_worker
from simple.benches.math import math_worker
from simple.benches.mgsm import mgsm_worker
from simple.benches.mmlu import mmlu_worker
from simple.benches.simpleqa import simpleqa_worker


logger = logging.getLogger("simple")

LOCK = asyncio.Lock()
CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent

BENCH_WORKERS = {
    "bbh": bbh_worker,
    "humaneval": humaneval_worker,
    "math": math_worker,
    "mgsm": mgsm_worker,
    "mmlu": mmlu_worker,
    "simpleqa": simpleqa_worker,
}
for bench in registry.BENCHES:
    assert bench.id in BENCH_WORKERS, f'No worker for "{bench.id}"'

ID_BENCHES = {_.id: _ for _ in registry.BENCHES}
ID_MODELS = {_.id: _ for _ in registry.MODELS}


async def worker(bench_id, model_id, model_client, task_item, res_item, context):
    context["in_progress"] += 1

    await BENCH_WORKERS[bench_id](model_client, task_item, res_item, context)
    res_item["finished_at"] = time.time()

    path = PROJ_DIR / "data" / "results" / bench_id / f"{model_id}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)

    async with LOCK:
        with path.open("a") as file:
            file.write(json.dumps(res_item, ensure_ascii=False) + "\n")

    context["in_progress"] -= 1
    context["bench_cost"] += res_item["bench_cost"]
    coef = 100 if ID_MODELS[model_id].currency == "rub" else 1
    context["model_cost"] += (res_item["model_cost"] / coef)
    logger.info(
        'is_correct=%r cost=%.5f+%.5f model="%s" bench="%s" task="%s"',
        int(res_item["is_correct"]),
        res_item["model_cost"], res_item["bench_cost"],
        model_id, bench_id, task_item["id"]
    )


async def monitor(context):
    count = 0
    while True:
        if not context["in_progress"]:
            break

        if count % 50 == 0:
            logger.info(
                "in_progress=%d cost=%.5f+%.5f",
                context["in_progress"], context["model_cost"], context["bench_cost"]
            )

        if count > 0 and count % 600 == 0:
            await update_context(context)

        count += 1
        await asyncio.sleep(.1)


async def init_context(context, bench_ids, model_ids):
    for bench_id in bench_ids:
        bench = ID_BENCHES[bench_id]
        for req in bench.reqs:
            if req in context:
                continue

            if req == "openrouter":
                api_key = os.getenv("OPENROUTER_API_KEY")
                assert api_key, f'Empty env var OPENROUTER_API_KEY, req by "{bench_id}"'
                context["openrouter"] = OpenrouterClient(api_key)

            elif req == "e2b":
                api_key = os.getenv("E2B_API_KEY")
                assert api_key, f'Empty env var E2B_API_KEY, req by "{bench_id}"'
                context["e2b"] = E2BClient(api_key)

            elif req == "bbh_prompts":
                path = PROJ_DIR / "data" / "benches" / "bbh_prompts.json"
                assert path.exists(), f'Non exist BBH prompts path "{path}"'
                with path.open() as file:
                    context["bbh_prompts"] = json.load(file)

            else:
                raise ValueError(req)

    for model_id in model_ids:
        model = ID_MODELS[model_id]
        if model.client in context:
            continue

        if model.client == "openrouter" and "openrouter" not in context:
            api_key = os.getenv("OPENROUTER_API_KEY")
            assert api_key, f'Empty env var OPENROUTER_API_KEY, req by "{model_id}"'
            context["openrouter"] = OpenrouterClient(api_key)

        elif model.client == "yandexgpt":
            api_key = os.getenv("YANDEXGPT_API_KEY")
            folder_id = os.getenv("YANDEXGPT_FOLDER_ID")
            assert api_key, f'Empty env var YANDEXGPT_API_KEY, req by "{model_id}""'
            assert api_key, f'Empty env var YANDEXGPT_FOLDER_ID, req by "{model_id}"'
            context["yandexgpt"] = YandexgptClient(api_key, folder_id)

        elif model.client == "gigachat":
            secret = os.getenv("GIGACHAT_SECRET")
            assert secret, f'Empty env var GIGACHAT_SECRET, req by "{model_id}"'
            context["gigachat"] = GigachatClient(secret)

        elif model.client == "runpod":
            api_key = os.getenv("RUNPOD_API_KEY")
            assert api_key, f'Empty env var RUNPOD_API_KEY, req by "{model_id}""'
            context["runpod"] = RunpodClient(api_key)

        else:
            raise ValueError(model.client)

    openrouter_client = context.get("openrouter")
    if openrouter_client:
        logger.info("Openrouter update model pricing")
        await openrouter_client.update_model_pricing()

    runpod_client = context.get("runpod")
    if runpod_client:
        logger.info("Runpod update model endpoints")
        await runpod_client.update_model_endpoints()

    for model_id in model_ids:
        model = ID_MODELS[model_id]

        if model.client == "openrouter" and openrouter_client:
            model_exists = model.client_model in openrouter_client.model_pricing
            assert model_exists, f'Openrouter non exist "{model.client_model}"'

        elif model.client == "runpod" and runpod_client:
            model_exists = model.client_model in runpod_client.model_endpoints
            assert model_exists, f'Runpod non exist "{model.client_model}"'


async def update_context(context):
    client = context.get("openrouter")
    if client:
        await client.update_rate_limit()
        logger.info(
            "Openrouter rate limit %d reqs / %d secs",
            client.rate_limiter.max_requests,
            client.rate_limiter.time_window
        )

    client = context.get("gigachat")
    if client:
        await client.update_oauth()
        logger.info(
            "Gigachat token expires in %d sec",
            client.expires_at - time.time()
        )


async def close_context(context):
    for key in ["openrouter", "yandexgpt", "gigachat", "e2b", "runpod"]:
        if key in context:
            await context[key].session.close()


def load_jsonl(path):
    with path.open() as file:
        for line in file:
            yield json.loads(line)


def load_task_items(bench_id, first_k=None):
    path = PROJ_DIR / "data" / "benches" / f"{bench_id}.jsonl"
    assert path.exists(), f'Non exist tasks path "{path}", bench "{bench_id}"'

    task_items = []
    for item in load_jsonl(path):
        task_items.append(item)
        if first_k is not None and len(task_items) >= first_k:
            break
    return task_items


def load_result_ids(bench_id, model_id):
    path = PROJ_DIR / "data" / "results" / bench_id / f"{model_id}.jsonl"

    result_ids = set()
    if path.exists():
        for item in load_jsonl(path):
            result_ids.add(item["id"])
    return result_ids


async def main(args):
    context = {
        "total": 0,
        "in_cache": 0,
        "in_progress": 0,
        "model_cost": 0,
        "bench_cost": 0,
    }
    try:
        await init_context(context, args.bench_ids, args.model_ids)
        await update_context(context)

        worker_coros = []
        for bench_id in args.bench_ids:
            task_items = load_task_items(bench_id, args.first_k_tasks)

            for model_id in args.model_ids:
                result_ids = load_result_ids(bench_id, model_id)

                for task_item in task_items:
                    context["total"] += 1
                    if task_item["id"] in result_ids:
                        context["in_cache"] += 1
                        continue

                    model = ID_MODELS[model_id]
                    model_client = partial(
                        context[model.client],
                        model=model.client_model,
                    )
                    res_item = {
                        "id": task_item["id"]
                    }
                    worker_coros.append(worker(
                        bench_id, model_id,
                        model_client, task_item, res_item,
                        context
                    ))

        random.shuffle(worker_coros)
        async with asyncio.TaskGroup() as task_group:
            for worker_coro in worker_coros:
                task_group.create_task(worker_coro)
            task_group.create_task(monitor(context))

        if context["total"] == 0:
            logger.into("Nothing to do, total=0")
        elif context["total"] == context["in_cache"]:
            logger.info("Nothing to do, total=in_cache=%d", context["in_cache"])

    finally:
        await close_context(context)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s [%(module)s:%(funcName)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger.setLevel(logging.DEBUG)

    bench_ids = sorted(_.id for _ in registry.BENCHES)
    model_ids = sorted(_.id for _ in registry.MODELS)

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="bench_ids", action="append", choices=bench_ids)
    parser.add_argument("-m", dest="model_ids", action="append", choices=model_ids)
    parser.add_argument("-k", dest="first_k_tasks", type=int)

    args = parser.parse_args()
    if not args.bench_ids:
        args.bench_ids = bench_ids
    if not args.model_ids:
        args.model_ids = model_ids
    asyncio.run(main(args))
