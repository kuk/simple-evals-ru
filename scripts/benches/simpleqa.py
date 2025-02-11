
import sys
import json
import random
import ast
from pathlib import Path

import pandas as pd


args = sys.argv[1:]
assert len(args) == 2, args
input_path, output_path = (Path(_) for _ in args)
assert input_path.exists(), input_path
assert output_path.parent.exists(), output_path


row_items = pd.read_csv(input_path).to_dict("records")
for index, item in enumerate(row_items):
    item["id"] = index

# {
#   "metadata": "{'topic': 'Video games', 'answer_type': 'Date', 'urls': ['https://www.aseprite.org/release-notes/', 'https://www.aseprite.org/release-notes/#:~:text=3%20November%2027%2C%202023,3.', 'https://blog.aseprite.org/2023/11/27/aseprite-v13/', 'https://store.steampowered.com/oldnews/?appids=431730&appgroupname=Aseprite&feed=steam_community_announcements']}",
#   "problem": "What were the day, month, and year of release for Aseprite v1.3?",
#   "answer": "27 Nov 2023",
#   "id": 1292
# }


random.seed(0)
random.shuffle(row_items)
assert len(row_items) >= 1000, len(row_items)

task_items = []
for item in row_items[:1000]:
    item["metadata"] = ast.literal_eval(item["metadata"])
    task_items.append({
        "id": item["id"],
        "problem": item["problem"],
        "target": item["answer"],
        "sources": item["metadata"]["urls"]
    })


with output_path.open("w") as file:
    for item in task_items:
        file.write(json.dumps(item, ensure_ascii=False))
        file.write("\n")
