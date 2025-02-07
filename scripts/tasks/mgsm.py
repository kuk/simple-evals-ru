
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
    for index, line in enumerate(file):
        parts = line.strip().split("\t")
        assert len(parts) == 2, parts
        problem, target = parts

        target = target.replace(",", "")
        assert target.isdigit(), target
        target = int(target)

        data.append({
            "id": index,
            "problem": problem,
            "target": target
        })


assert len(data) == 250, len(data)
with output_path.open("w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
