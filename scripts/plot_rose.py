
import json
from pathlib import Path

import numpy as np

from matplotlib import pyplot as plt

from simple.registry import (
    MODELS,
    BENCHES
)

ID_MODELS = {_.id: _ for _ in MODELS}

CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent


fig, (ax1, ax2) = plt.subplots(
    1, 2,
    subplot_kw={"projection": "polar"}
)
bench_thetas = np.arange(0, 2 * np.pi, 2 * np.pi / len(BENCHES))


def plot(ax, title, model_ids):
    for model_id in model_ids:
        model = ID_MODELS[model_id]

        rs, rs1, rs2 = [], [], []
        for bench in BENCHES:
            results = []
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model_id}.jsonl"
            with path.open() as file:
                for line in file:
                    item = json.loads(line)
                    results.append(item["is_correct"])

            results = np.array(results)
            bs_means = []
            for _ in range(100):
                sample = np.random.choice(results, size=len(results), replace=True)
                bs_means.append(sample.mean())

            rs.append(np.mean(results))
            rs1.append(np.percentile(bs_means, 5))
            rs2.append(np.percentile(bs_means, 95))

        thetas = bench_thetas.copy()
        thetas = np.append(thetas, thetas[0])
        rs.append(rs[0])
        rs1.append(rs1[0])
        rs2.append(rs2[0])
        ax.plot(thetas, rs, label=model.name)
        ax.fill_between(thetas, rs1, rs2, alpha=0.2)

    ax.spines.polar.set_visible(False)
    ax.yaxis.grid(linestyle=":")
    ax.xaxis.grid(linestyle=":")

    ax.set_xticks(bench_thetas, [_.name for _ in BENCHES])

    ax.set_ylim(0, 1)
    values = np.arange(0, 1.1, 0.2)
    ax.set_yticks(values)
    ax.set_yticklabels([f"{_:0.1f}" for _ in values])

    ax.legend(
        loc="lower center",
        ncol=2,
        bbox_to_anchor=(0.5, -0.3),
        frameon=False
    )

    ax.set_title(title)


plot(ax1, "lite", [
    "10_llama_3_1_8b",
    "07_yandexgpt_4_lite",
    "08_gigachat_lite",
])
plot(ax2, "pro", [
    # "13_llama_3_3_70b",
    # "11_yandexgpt_4_pro",
    # "12_gigachat_pro",
    "14_gigachat_max",

    
    "17_yandexgpt_5_pro",
    "20_t_pro",
])

# "04_llama_3_1_8b",
# "10_llama_3_1_8b",

# "05_llama_3_3_70b",
# "13_llama_3_3_70b",


fig.set_size_inches(8, 4)
fig.tight_layout()

path = PROJ_DIR / "images" / "rose.svg"
print('Write "%s"' % path)
path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(path, format="svg")
