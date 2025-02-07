
import sys
import json
from pathlib import Path


args = sys.argv[1:]
assert len(args) == 2, args
input_path, output_path = (Path(_) for _ in args)
assert input_path.exists(), input_path
assert output_path.parent.exists(), output_path


data = []
with input_path.open() as file:
    for line in file:
        item = json.loads(line)
        data.append({
            "id": item["task_id"],
            "prompt": item["prompt"],
            "canonical_solution": item["canonical_solution"],
            "entry_point": item["entry_point"],
            "test": item["test"],
        })
assert len(data) == 164, len(data)


with output_path.open("w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
