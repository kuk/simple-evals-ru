
import re
import sys
import json
import argparse
import logging
from pathlib import Path
from contextlib import contextmanager

from simple.registry import (
    MODELS,
    BENCHES
)


CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent

ID_MODELS = {_.id: _ for _ in MODELS}
ID_BENCHES = {_.id: _ for _ in BENCHES}


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

    bench_ids = sorted(_.id for _ in BENCHES)
    model_ids = sorted(_.id for _ in MODELS)

    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="bench_ids", action="append", choices=bench_ids)
    parser.add_argument("-m", dest="model_ids", action="append", choices=model_ids)

    args = parser.parse_args()

    bench_model_res_items = {}
    for bench_id in bench_ids:
        for model_id in model_ids:
            path = PROJ_DIR / "data" / "results" / bench_id / f"{model_id}.jsonl"
            if path.exists():
                res_items = [_ for _ in load_jsonl(path) if not _["is_correct"]]
                if res_items:
                    bench_model_res_items[bench_id, model_id] = res_items

    if not bench_model_res_items:
        logging.info("No error results")
        sys.exit()

    bench_id_task_items = {}
    for bench_id in bench_ids:
        path = PROJ_DIR / "data" / "benches" / f"{bench_id}.jsonl"
        assert path.exists(), path
        task_items = load_jsonl(path)
        bench_id_task_items[bench_id] = {_["id"]: _ for _ in task_items}

    for model_id in model_ids:
        for bench_id in bench_ids:
            id_task_items = bench_id_task_items[bench_id]

            res_items = bench_model_res_items.get((bench_id, model_id))
            if not res_items:
                continue

            path = PROJ_DIR / "errors" / bench_id / f"{model_id}.md"
            path.parent.mkdir(parents=True, exist_ok=True)

            logging.info('Write len(res_items)=%d, path="%s"', len(res_items), path.relative_to(PROJ_DIR))
            with path.open("w") as file, print_to(file):
                print("#", ID_BENCHES[bench_id].name, "/", ID_MODELS[model_id].name)

                res_items.sort(key=lambda _: _["finished_at"], reverse=True)
                for res_item in res_items[:20]:
                    task_item = id_task_items[res_item["id"]]
                    print_result(bench_id, task_item, res_item)
