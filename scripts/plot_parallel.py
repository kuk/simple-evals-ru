

import json
from pathlib import Path

from matplotlib import pyplot as plt

from simple.registry import (
    MODELS,
    BENCHES
)

ID_MODELS = {_.id: _ for _ in MODELS}

CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent


path = PROJ_DIR / "data" / "stats.json"
with path.open() as file:
    data = json.load(file)


def plot(title, model_ids, filename):
    fig, ax = plt.subplots()

    for x in range(len(BENCHES)):
        ax.axvline(x=x, color="silver", linestyle=":", linewidth=1)

    for model_id in model_ids:
        model = ID_MODELS[model_id]

        ys, ys1, ys2 = [], [], []
        for bench in BENCHES:
            stats = data["bench_model_stats"][bench.id][model_id]
            y = stats["score"]
            std = stats["std"]
            ys.append(y)
            ys1.append(y - std)
            ys2.append(y + std)

        xs = range(len(BENCHES))
        ax.plot(xs, ys, label=model.name)
        ax.fill_between(xs, ys1, ys2, alpha=0.2)

    ax.set_xticks(xs, [_.name for _ in BENCHES])
    ax.set_title(title)

    ax.set_ylabel("bench score")

    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    fig.set_size_inches(8, 4)
    fig.tight_layout()

    path = PROJ_DIR / "images" / filename
    print('Write "%s"' % path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg")


plot("yandexgpt 8b base", [
    "21_saiga",
    "22_vikhr",
], "parallel1.svg")

plot("qwen 32b base", [
    "17_yandexgpt_5_pro",
    "20_t_pro",
    "29_ruadapt",
    "28_qwen_2_5_32b",
], "parallel2.svg")

plot("yandexgpt / gigachat", [
    "17_yandexgpt_5_pro",
    "26_gigachat_pro",
    "27_gigachat_max",
], "parallel3.svg")

plot("qwen 7b base", [
    "19_t_lite",
    "06_qwen_2_5_7b",
], "parallel4.svg")

plot("ruadapt", [
    "20_t_pro",
    "24_ruadapt",
    "29_ruadapt",
    "28_qwen_2_5_32b",
], "parallel5.svg")

