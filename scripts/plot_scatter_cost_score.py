
import json
from pathlib import Path

import numpy as np

from matplotlib import pyplot as plt
from matplotlib.ticker import (
    MaxNLocator,
    FuncFormatter
)
from adjustText import adjust_text

from simple.registry import (
    MODELS,
    BENCHES
)

ID_MODELS = {_.id: _ for _ in MODELS}

CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent


xs, yerrs1, yerrs2, ys, labels = [], [], [], [], []
for model_id in [
        "01_gemini_flash_1_5", "02_llama_3_2_1b",
        "03_llama_3_2_3b", "04_llama_3_1_8b",
        "05_llama_3_3_70b", "06_qwen_2_5_7b",
        "07_yandexgpt_4_lite", "08_gigachat_lite",
        "09_yandexgpt_3_lite", "10_llama_3_1_8b",
]:
    model = ID_MODELS[model_id]

    tokens, cost = 0, 0
    results = []

    for bench in BENCHES:
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

    if model.currency == "rub":
        cost /= 100

    x = cost / tokens * 1_000_000
    xs.append(x)

    results = np.array(results)
    bs_means = []
    for _ in range(100):
        sample = np.random.choice(results, size=len(results), replace=True)
        bs_means.append(sample.mean())

    y = np.mean(results)
    lower = np.percentile(bs_means, 5)
    upper = np.percentile(bs_means, 95)

    ys.append(y)
    yerrs1.append(upper - y)
    yerrs2.append(y - lower)
    labels.append(model.name)

fig, ax = plt.subplots()
ax.errorbar(
    xs, ys,
    yerr=[yerrs1, yerrs2],
    fmt=".",
    linewidth=1,
)

texts = []
for x, y, label in zip(xs, ys, labels):
    text = ax.text(x, y, label)
    texts.append(text)

adjust_text(texts)

ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
ax.xaxis.set_major_formatter(FuncFormatter("${:.1f}".format))
ax.set_xlabel("cost per 1m input + output tokens")

ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
ax.yaxis.set_major_formatter(FuncFormatter("{:.1f}".format))
ax.set_ylim(0, 1)
ax.set_ylabel(
    f"avg score on {len(BENCHES)} benches: math-500, humaneval, ...\n"
    "bootstrap conf intervals"
)

path = PROJ_DIR / "images" / "cost_score.svg"
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
