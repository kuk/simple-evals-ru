
import re
import sys
import json
import argparse
import logging
from pathlib import Path
from contextlib import contextmanager

from simple import registry


CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent


@contextmanager
def print_to(file):
    orig_stdout = sys.stdout
    try:
        sys.stdout = file
        yield
    finally:
        sys.stdout = orig_stdout


def print_section(item, key):
    print(f"###### {key}")
    print("<pre>", re.sub(r"</?pre>", "", str(item[key])), "</pre>")


def print_result(bench_id, task_item, res_item):
    print("###", task_item["id"])

    if bench_id == "humaneval":
        print_section(res_item, "instruction")
        print_section(res_item, "answer")

        print_section(res_item, "pred")
        print_section(task_item, "canonical_solution")
        print_section(task_item, "test")

        if res_item["timed_out"]:
            res_item["traceback"] = "Timed out"

        if res_item["traceback"]:
            print_section(res_item, "traceback")

    elif bench_id == "simpleqa":
        print_section(res_item, "instruction")
        print_section(res_item, "answer")
        print_section(task_item, "target")
        print_section(res_item, "judge_pred")

    else:
        print_section(res_item, "instruction")
        print_section(res_item, "answer")
        print_section(res_item, "pred")
        print_section(task_item, "target")


def load_jsonl(path):
    with path.open() as file:
        for line in file:
            yield json.loads(line)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    bench_ids = sorted(_.id for _ in registry.BENCHES)
    model_ids = sorted(_.id for _ in registry.MODELS)

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bench", dest="bench_ids", action="append", choices=bench_ids)
    parser.add_argument("-m", "--model", dest="model_ids", action="append", choices=model_ids)

    args = parser.parse_args()
    if args.bench_ids:
        bench_ids = args.bench_ids
    if args.model_ids:
        model_ids = args.model_ids

    id_benches = {_.id: _ for _ in registry.BENCHES}
    id_models = {_.id: _ for _ in registry.MODELS}
    benches = [id_benches[_] for _ in bench_ids]
    models = [id_models[_] for _ in model_ids]

    bench_model_res_items = {}
    for bench in registry.BENCHES:
        for model in registry.MODELS:
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
            if path.exists():
                res_items = [_ for _ in load_jsonl(path) if not _["is_correct"]]
                if res_items:
                    bench_model_res_items[bench.id, model.id] = res_items

    if not bench_model_res_items:
        logging.info("No error results")
        sys.exit()

    bench_id_task_items = {}
    for bench in registry.BENCHES:
        path = PROJ_DIR / "data" / "benches" / f"{bench.id}.jsonl"
        assert path.exists(), path
        task_items = load_jsonl(path)
        bench_id_task_items[bench.id] = {_["id"]: _ for _ in task_items}

    for model in models:
        for bench in benches:
            id_task_items = bench_id_task_items[bench.id]

            res_items = bench_model_res_items.get((bench.id, model.id))
            if not res_items:
                continue

            path = PROJ_DIR / "errors" / bench.id / f"{model.id}.md"
            path.parent.mkdir(parents=True, exist_ok=True)

            logging.info('Write len(res_items)=%d, path="%s"', len(res_items), path.relative_to(PROJ_DIR))
            with path.open("w") as file, print_to(file):
                print("#", bench.name, "/", model.name)

                res_items.sort(key=lambda _: _["finished_at"], reverse=True)
                for res_item in res_items[:20]:
                    task_item = id_task_items[res_item["id"]]
                    print_result(bench.id, task_item, res_item)
