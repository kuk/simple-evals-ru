
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
    "other": "tab:blue",
    "openrouter": "tab:orange",
}


xs, ys, colors, labels = [], [], [], []
model_xys = {}
for model_id in [
        "04_llama_3_1_8b",
        "10_llama_3_1_8b",
        "05_llama_3_3_70b",
        "13_llama_3_3_70b",

        "15_qwen_2_5_72b",
        "16_deepseek_v3",

        "07_yandexgpt_4_lite", "08_gigachat_lite",
        "11_yandexgpt_4_pro", "12_gigachat_pro", "14_gigachat_max",
]:
    model = ID_MODELS[model_id]

    tokens, cost = 0, 0
    scores = []
    for bench in BENCHES:
        results = []

        path = PROJ_DIR / "data" / "results" / bench.id / f"{model_id}.jsonl"
        with path.open() as file:
            for line in file:
                item = json.loads(line)

                results.append(item["is_correct"])

                for key in ["total_tokens", "totalTokens"]:
                    if key in item["usage"]:
                        tokens += item["usage"][key]
                        break
                else:
                    raise ValueError(item["usage"])

                cost += item["model_cost"]
        score = np.mean(results)
        scores.append(score)

    if model.currency == "rub":
        cost /= 100

    x = cost / tokens * 1_000_000
    xs.append(x)

    y = np.mean(scores)
    ys.append(y)

    group = "other"
    if model.client == "openrouter":
        group = "openrouter"
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
x1, y1 = model_xys["04_llama_3_1_8b"]
x2, y2 = model_xys["10_llama_3_1_8b"]
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
x1, y1 = model_xys["05_llama_3_3_70b"]
x2, y2 = model_xys["13_llama_3_3_70b"]
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

ta.allocate(
    ax, xs, ys,
    labels,
    x_scatter=xs, y_scatter=ys,
    x_lines=x_lines, y_lines=y_lines,
    linecolor="silver",
    avoid_crossing_label_lines=True,
    ylims=(0.2, 1)
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

ax.set_ylim(0.2, 1)
values = np.arange(0.2, 1.1, 0.2)
ax.set_yticks(values)
ax.set_yticklabels([f"{_:0.1f}" for _ in values])
ax.set_ylabel(f"avg score on {len(BENCHES)} benches: math-500, humaneval, ..")

ax.set_title("ru vs world")

path = PROJ_DIR / "images" / "cost_score2.svg"
print('Write "%s"' % path)
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
