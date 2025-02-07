
import sys
import json
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


data = []
index = 0
for row_item in pd.read_csv(input_path).to_dict("records"):
    if row_item["Question"] not in select_problems:
        continue

    data.append({
        "id": index,
        "problem": row_item["Question"],
        "target": row_item["Answer"],
    })
    index += 1
assert len(data) == 500, len(data)


with output_path.open("w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
