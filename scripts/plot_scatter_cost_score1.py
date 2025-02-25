
import re
import json
from pathlib import Path

import numpy as np

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
    "yandexgpt": "tab:blue",
    "t_pro": "tab:purple",
    "gigachat": "tab:orange",
}


path = PROJ_DIR / "data" / "stats.json"
with path.open() as file:
    data = json.load(file)


xs, ys, yerrs, colors, labels = [], [], [], [], []
for model_id in [
        "07_yandexgpt_4_lite", "08_gigachat_lite",
        # "10_llama_3_1_8b",

        "11_yandexgpt_4_pro", "12_gigachat_pro",
        # "13_llama_3_3_70b",
        "14_gigachat_max",

        "17_yandexgpt_5_pro",

        # "18_cotype_nano",
        # "19_t_lite",
        "20_t_pro",
]:
    model = ID_MODELS[model_id]

    stats = data["model_stats"][model_id]
    x = stats["cost"] / stats["tokens"] * 1_000_000
    xs.append(x)

    y = stats["avg_score"]
    std = stats["avg_std"]

    ys.append(y)
    yerrs.append(std)

    match = re.search(r"(yandexgpt|gigachat|t_pro)", model_id)
    assert match, model_id
    group = match.group(1)
    color = GROUP_COLORS[group]
    colors.append(color)

    labels.append(model.name)

fig, ax = plt.subplots()
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
    draw_lines=False
)

values = sorted({round(_, 1) for _ in xs})
ax.set_xticks(values)
ax.set_xticklabels([f"{_:0.1f}$" for _ in values])
ax.set_xlabel("cost per 1m input + output tokens")

ax.set_ylim(0.2, 1)
values = np.arange(0.2, 1.1, 0.2)
ax.set_yticks(values)
ax.set_yticklabels([f"{_:0.2f}" for _ in values])
ax.set_ylabel(f"avg score on {len(BENCHES)} benches: math-500, humaneval, ..")

ax.set_title("ru")

path = PROJ_DIR / "images" / "cost_score1.svg"
print('Write "%s"' % path)
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
