
import sys
import json
import random
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


def escape(value):
    value = str(value)
    return value.replace("<", "&lt;")


def print_section(item, key):
    print(f"###### {key}")
    print("<pre>", escape(item[key]), "</pre>")


def print_result(bench_id, task_item, res_item):
    print("###", task_item["id"])

    if bench_id in ("humaneval", "mbpp"):
        print_section(res_item, "instruction")
        print_section(res_item, "answer")

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
    items = []
    with path.open() as file:
        for line in file:
            items.append(json.loads(line))
    return items


if __name__ == "__main__":
    bench_model_res_items = {}
    for bench in BENCHES:
        for model in MODELS:
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
            res_items = []
            if path.exists():
                res_items = load_jsonl(path)
            bench_model_res_items[bench.id, model.id] = res_items

    bench_id_task_items = {}
    for bench in BENCHES:
        path = PROJ_DIR / "data" / "benches" / f"{bench.id}.jsonl"
        assert path.exists(), path
        bench_id_task_items[bench.id] = {_["id"]: _ for _ in load_jsonl(path)}

    for model in MODELS:
        for bench in BENCHES:
            id_task_items = bench_id_task_items[bench.id]

            res_items = bench_model_res_items[bench.id, model.id]
            for section in ["correct", "errors"]:
                path = PROJ_DIR / "reports" / section / bench.id / f"{model.id}.md"
                path.parent.mkdir(parents=True, exist_ok=True)

                section_items = [
                    _ for _ in res_items
                    if _["is_correct"] == (section == "correct")
                ]
                print(
                    'Write len(section_items)=%d, path="%s"'
                    % (len(section_items), path.relative_to(PROJ_DIR))
                )
                with path.open("w") as file, print_to(file):
                    print("#", ID_BENCHES[bench.id].name, "/", ID_MODELS[model.id].name)

                    if section == "correct":
                        random.seed(0)
                        random.shuffle(section_items)
                        cap = 10
                    elif section == "errors":
                        section_items.sort(key=lambda _: _["finished_at"], reverse=True)
                        cap = 20

                    for res_item in section_items[:cap]:
                        task_item = id_task_items[res_item["id"]]
                        print_result(bench.id, task_item, res_item)
