
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
    for index, line in enumerate(file):
        parts = line.strip().split("\t")
        assert len(parts) == 2, parts
        problem, target = parts

        target = target.replace(",", "")
        assert target.isdigit(), target
        target = int(target)

        task_items.append({
            "id": index,
            "problem": problem,
            "target": target
        })
assert len(task_items) == 250, len(task_items)


random.seed(0)
random.shuffle(task_items)

with output_path.open("w") as file:
    for item in task_items:
        file.write(json.dumps(item, ensure_ascii=False))
        file.write("\n")
