
import os
import json
import asyncio
import logging
import time
from collections import Counter
from pathlib import Path
from functools import partial

from simple import registry

from simple.clients.openrouter import OpenrouterClient
from simple.clients.yandexgpt import YandexgptClient
from simple.clients.gigachat import GigachatClient
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


async def worker(bench_id, model_id, model_client, task_item, res_item, context):
    context["in_progress"][bench_id, model_id] += 1

    await BENCH_WORKERS[bench_id](model_client, task_item, res_item, context)
    res_item["finished_at"] = time.time()

    path = CUR_DIR / "data" / "results" / bench_id / f"{model_id}.jsonl"
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    async with LOCK:
        with path.open("a") as file:
            file.write(json.dumps(res_item, ensure_ascii=False) + "\n")

    context["in_progress"][bench_id, model_id] -= 1
    logger.info(
        'RES bench="%s" model="%s" task="%s" is_correct=%r cost=%.5f+%.5f',
        bench_id, model_id, task_item["id"],
        int(res_item["is_correct"]),
        res_item["model_cost"], res_item["bench_cost"]
    )


async def monitor(context):
    count = 0
    while True:
        in_progress = sum(context["in_progress"].values())
        if not in_progress:
            break

        if count % 50 == 0:
            logger.info("MON in_progress=%d", in_progress)
        count += 1
        await asyncio.sleep(.1)


def init_context():
    context = {
        "in_progress": Counter()
    }

    for bench in registry.BENCHES:
        for req in bench.reqs:
            if req in context:
                continue

            if req == "openrouter":
                api_key = os.getenv("OPENROUTER_API_KEY")
                assert api_key, f'Empty env var OPENROUTER_API_KEY, req by "{bench.id}"'
                context["openrouter"] = OpenrouterClient(api_key)

            elif req == "e2b":
                api_key = os.getenv("E2B_API_KEY")
                assert api_key, f'Empty env var E2B_API_KEY, req by "{bench.id}"'
                context["e2b"] = E2BClient(api_key)

            elif req == "bbh_prompts":
                path = CUR_DIR / "data" / "benches" / "bbh_prompts.json"
                assert path.exists(), f'Non exist BBH prompts path "{path}"'
                with path.open() as file:
                    context["bbh_prompts"] = json.load(file)

            else:
                raise ValueError(req)

    for model in registry.MODELS:
        if model.client in context:
            continue

        if model.client == "openrouter" and "openrouter" not in context:
            api_key = os.getenv("OPENROUTER_API_KEY")
            assert api_key, f'Empty env var OPENROUTER_API_KEY, req by "{model.id}"'
            context["openrouter"] = OpenrouterClient(api_key)

        if model.client == "yandexgpt":
            api_key = os.getenv("YANDEXGPT_API_KEY")
            folder_id = os.getenv("YANDEXGPT_FOLDER_ID")
            assert api_key, f'Empty env var YANDEXGPT_API_KEY, req by "{model.id}""'
            assert api_key, f'Empty env var YANDEXGPT_FOLDER_ID, req by "{model.id}"'
            context["yandexgpt"] = YandexgptClient(api_key, folder_id)

        if model.client == "gigachat":
            secret = os.getenv("GIGACHAT_SECRET")
            assert secret, f'Empty env var GIGACHAT_SECRET, req by "{model.id}"'
            context["gigachat"] = GigachatClient(secret)

        else:
            raise ValueError(model.client)

    return context


async def close_context(context):
    for key in ["openrouter", "yandexgpt", "gigachat", "e2b"]:
        if key in context:
            await context[key].session.close()


def load_task_items(bench_id):
    path = CUR_DIR / "data" / "benches" / f"{bench_id}.jsonl"
    assert path.exists(), f'Non exist tasks path "{path}", bench "{bench_id}"'

    task_items = []
    with path.open() as file:
        for line in file:
            task_items.append(json.loads(line))
            if len(task_items) >= 1:
                break
    return task_items


def load_result_ids(bench_id, model_id):
    path = CUR_DIR / "results" / bench_id / f"{model_id}.jsonl"

    result_ids = set()
    if path.exists():
        with path.open() as file:
            for line in file:
                item = json.loads(line)
                result_ids.add(item["id"])
    return result_ids


async def main():
    context = None
    try:
        context = init_context()
        async with asyncio.TaskGroup() as task_group:
            for bench in registry.BENCHES:
                task_items = load_task_items(bench.id)

                for model in registry.MODELS:
                    result_ids = load_result_ids(bench.id, model.id)
                    for task_item in task_items:
                        if task_item["id"] in result_ids:
                            continue

                        client_model = partial(
                            context[model.client],
                            model=model.client_model
                        )
                        res_item = {
                            "id": task_item["id"]
                        }
                        task_group.create_task(worker(
                            bench.id, model.id,
                            client_model, task_item, res_item,
                            context
                        ))
            task_group.create_task(monitor(context))

    finally:
        if context:
            await close_context(context)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger.setLevel(logging.DEBUG)

    asyncio.run(main())
