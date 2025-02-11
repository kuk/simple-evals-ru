
import re
import sys
import json
import random
from pathlib import Path
from contextlib import contextmanager

from simple import registry


PROJ_DIR = Path(__file__).parent.parent


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

    if res_item["is_correct"]:
        res_item["verdict"] = "✅ PASS"
    else:
        res_item["verdict"] = "❌ FAIL"
    print_section(res_item, "verdict")


def load_jsonl(path):
    items = []
    with path.open() as file:
        for line in file:
            items.append(json.loads(line))
    return items


bench_id_task_items = {}
for bench in registry.BENCHES:
    path = PROJ_DIR / "data" / "benches" / f"{bench.id}.jsonl"
    assert path.exists(), path
    task_items = load_jsonl(path)
    bench_id_task_items[bench.id] = {_["id"]: _ for _ in task_items}

bench_model_res_items = {}
for bench in registry.BENCHES:
    for model in registry.MODELS:
        path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
        assert path.exists(), path
        bench_model_res_items[bench.id, model.id] = load_jsonl(path)

for model in registry.MODELS:
    path = PROJ_DIR / "reports" / f"{model.id}.md"
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as file, print_to(file):
        print("#", model.name)

        for bench in registry.BENCHES:
            print("##", bench.name)

            id_task_items = bench_id_task_items[bench.id]
            res_items = bench_model_res_items[bench.id, model.id]

            random.seed(0)
            random.shuffle(res_items)

            for res_item in res_items[:10]:
                task_item = id_task_items[res_item["id"]]
                print_result(bench.id, task_item, res_item)
