
import sys
import json
import random
from pathlib import Path


args = sys.argv[1:]
assert len(args) == 2, args
input_path, output_path = (Path(_) for _ in args)
assert input_path.exists(), input_path
assert output_path.parent.exists(), output_path


task_items = []
with input_path.open() as file:
    for line in file:
        item = json.loads(line)
        task_items.append({
            "id": item["task_id"],
            "prompt": item["prompt"],
            "canonical_solution": item["canonical_solution"],
            "entry_point": item["entry_point"],
            "test": item["test"],
        })
assert len(task_items) == 164, len(task_items)


random.seed(0)
random.shuffle(task_items)

with output_path.open("w") as file:
    for item in task_items:
        file.write(json.dumps(item, ensure_ascii=False))
        file.write("\n")
