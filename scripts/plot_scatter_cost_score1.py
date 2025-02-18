
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
    "llama": "tab:blue",
    "gigachat": "tab:orange",
}


xs, ys, yerrs, colors, labels = [], [], [], [], []
for model_id in [
        "07_yandexgpt_4_lite", "08_gigachat_lite",
        "10_llama_3_1_8b",

        "11_yandexgpt_4_pro", "12_gigachat_pro",
        "13_llama_3_3_70b", "14_gigachat_max",

]:
    model = ID_MODELS[model_id]

    tokens, cost = 0, 0
    scores, stds = [], []
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

        results = np.array(results)
        bs_means = []
        for _ in range(100):
            sample = np.random.choice(results, size=len(results), replace=True)
            bs_means.append(sample.mean())

        score = np.mean(results)
        std1 = score - np.percentile(bs_means, 5)
        std2 = np.percentile(bs_means, 95) - score
        assert std1 >= 0, std1
        assert std2 >= 0, std2
        std = (std1 + std2) / 2
        scores.append(score)
        stds.append(std)

    if model.currency == "rub":
        cost /= 100

    x = cost / tokens * 1_000_000
    xs.append(x)

    y = np.mean(scores)
    std = np.sqrt(np.mean([_**2 for _ in stds]))

    ys.append(y)
    yerrs.append(std)

    match = re.search(r"(yandexgpt|gigachat|llama)", model_id)
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
values = sorted({round(_, 2) for _ in ys} | {0.2, 1})
ax.set_yticks(values)
ax.set_yticklabels([f"{_:0.2f}" for _ in values])
ax.set_ylabel(f"avg score on {len(BENCHES)} benches: math-500, humaneval, ..")

ax.set_title("yandexgpt vs gigachat")

path = PROJ_DIR / "images" / "cost_score1.svg"
print('Write "%s"' % path)
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
