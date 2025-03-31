
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
    "yandexgpt-4": "silver",
    "gigachat": "silver",
    "yandexgpt-5": "tab:blue",
    "gigachat-2": "tab:orange",
}
GROUP_PATTERN = "(" + "|".join(sorted(GROUP_COLORS.keys(), key=len, reverse=True)) + ")"


path = PROJ_DIR / "data" / "stats.json"
with path.open() as file:
    data = json.load(file)


xs, ys, yerrs, colors, labels = [], [], [], [], []
for model_id in [
        "07_yandexgpt_4_lite", "08_gigachat_lite",
        "25_gigachat_lite", "30_yandexgpt_5_lite",

        "11_yandexgpt_4_pro", "12_gigachat_pro",
        "17_yandexgpt_5_pro", "26_gigachat_pro",

        "27_gigachat_max",
        "14_gigachat_max",
]:
    model = ID_MODELS[model_id]

    stats = data["model_stats"][model_id]
    x = stats["cost"] / stats["tokens"] * 1_000_000
    xs.append(x)

    y = stats["avg_score"]
    std = stats["avg_std"]

    ys.append(y)
    yerrs.append(std)

    match = re.search(GROUP_PATTERN, model.name)
    assert match, model.name
    group = match.group(0)
    color = GROUP_COLORS[group]
    colors.append(color)
    labels.append(model.name)

fig, ax = plt.subplots()
ax.set_ylim(.25, .85)

ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())

ys2, labels2 = [], []
for model_id in ["21_saiga", "20_t_pro"]:
    model = ID_MODELS[model_id]

    y = data["model_stats"][model_id]["avg_score"]
    ax2.axhline(y=y, color="silver", linestyle=":", linewidth=1)

    ys2.append(y)
    labels2.append(model.name)

ax2.set_yticks(ys2)
ax2.set_yticklabels(labels2)

for x, y, yerr, color in zip(xs, ys, yerrs, colors):
    ax.errorbar(
        x, y,
        yerr=yerr,
        color=color,
        fmt="o",
    )

ta.allocate(
    ax, xs, ys,
    labels,
    x_scatter=xs, y_scatter=ys,
    linecolor="silver",
    avoid_crossing_label_lines=True,
    ylims=ax.get_ylim()
)

values = sorted({round(_, 1) for _ in xs})
ax.set_xticks(values)
ax.set_xticklabels([f"{_:0.1f}$" for _ in values])

ax.set_xlabel("cost per 1m input + output tokens")
ax.set_ylabel(f"avg score on {len(BENCHES)} benches: math-500, humaneval, ..")
ax.set_title("gigachat / yandexgpt")

fig.set_size_inches(8, 5)
fig.tight_layout()

path = PROJ_DIR / "images" / "cost_score1.svg"
print('Write "%s"' % path)
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
