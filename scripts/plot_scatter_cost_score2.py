
import re
import json
from pathlib import Path

from matplotlib import pyplot as plt


import textalloc as ta

from simple.registry import (
    MODELS,
    BENCHES
)

ID_MODELS = {_.id: _ for _ in MODELS}

CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent

GROUP_COLORS = {
    "qwen": "tab:orange",
    "deepseek": "tab:orange",

    "yandexgpt-5": "tab:blue",
    "yandexgpt-4-lite": "tab:blue",
    "gigachat-2": "tab:blue",

    "yandexgpt-4": "silver",
    "gigachat": "silver",
}
GROUP_PATTERN = "(" + "|".join(sorted(GROUP_COLORS.keys(), key=len, reverse=True)) + ")"

path = PROJ_DIR / "data" / "stats.json"
with path.open() as file:
    data = json.load(file)


xs, ys, colors, labels = [], [], [], []
model_xys = {}
for model_id in [
        "06_qwen_2_5_7b",
        "15_qwen_2_5_72b",
        "28_qwen_2_5_32b",
        "16_deepseek_v3",

        "08_gigachat_lite",
        "12_gigachat_pro",
        "14_gigachat_max",
        "25_gigachat_lite",
        "26_gigachat_pro",
        "27_gigachat_max",

        "11_yandexgpt_4_pro",
        "17_yandexgpt_5_pro",
]:
    model = ID_MODELS[model_id]

    stats = data["model_stats"][model_id]
    x = stats["cost"] / stats["tokens"] * 1_000_000
    xs.append(x)

    y = stats["avg_score"]
    ys.append(y)

    match = re.search(GROUP_PATTERN, model.name)
    assert match, model.name
    group = match.group(0)
    color = GROUP_COLORS[group]
    colors.append(color)

    labels.append(model.name)
    model_xys[model_id] = (x, y)

fig, ax = plt.subplots()
ax.scatter(
    xs, ys,
    color=colors
)

x_lines, y_lines = [], []
x1, y1 = model_xys["28_qwen_2_5_32b"]
x2, y2 = model_xys["17_yandexgpt_5_pro"]
ax.plot(
    [x1, x2],
    [y1, y2],
    linestyle=":",
    linewidth=1,
    color="silver"
)
x_lines.append((x1, x2))
y_lines.append((y1, y2))
ax.text(
    (x1 + x2) / 2,
    (y1 + y2) / 2,
    f"x{x2 / x1:0.0f}",
    va="center",
    ha="center",
)

ax.set_ylim(.35, .99)
ta.allocate(
    ax, xs, ys,
    labels,
    x_scatter=xs, y_scatter=ys,
    x_lines=x_lines, y_lines=y_lines,
    linecolor="silver",
    avoid_crossing_label_lines=True,
    ylims=ax.get_ylim()
)


values = sorted({round(_, 1) for _ in xs})
ax.set_xticks(values)

labels = []
for value in values:
    if value < 1:
        labels.append("")
    else:
        labels.append(f"{value:0.1f}$")
ax.set_xticklabels(labels)

ax.set_xlabel("cost per 1m input + output tokens")
ax.set_ylabel(f"avg score on {len(BENCHES)} benches: math-500, humaneval, ..")
ax.set_title("ru vs world")

fig.set_size_inches(6, 5)
fig.tight_layout()

path = PROJ_DIR / "images" / "cost_score2.svg"
print('Write "%s"' % path)
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
