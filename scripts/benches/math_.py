
import sys
import json
import random
from pathlib import Path

import pandas as pd


args = sys.argv[1:]
assert len(args) == 3, args
input_path, input_500_path, output_path = (Path(_) for _ in args)
assert input_path.exists(), input_path
assert input_500_path.exists(), input_path
assert output_path.parent.exists(), output_path


row_items = pd.read_csv(input_500_path).to_dict("records")
select_problems = {_["Question"] for _ in row_items}
assert len(select_problems) == 500, len(select_problems)


row_items = pd.read_csv(input_path).to_dict("records")
task_items = []
for index, item in enumerate(row_items):
    item["id"] = index

    if item["Question"] not in select_problems:
        continue

    task_items.append({
        "id": item["id"],
        "problem": item["Question"],
        "target": item["Answer"],
    })
assert len(task_items) == 500, len(task_items)


random.seed(0)
random.shuffle(task_items)

with output_path.open("w") as file:
    for item in task_items:
        file.write(json.dumps(item, ensure_ascii=False))
        file.write("\n")
