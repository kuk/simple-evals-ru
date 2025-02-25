
import json
from pathlib import Path
from collections import defaultdict

import numpy as np

from simple.registry import (
    MODELS,
    BENCHES,
)


CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent

RUNPOD_COSTS = {
    "20_t_pro": 1.351 + 3.069 + 1.635 + 0.677,
    "19_t_lite": 0.434 + 0.732 + 0.031 + 0.017,
    "18_cotype_nano": 0.032 + 0.622 + 0.034 + 0.031,
}


if __name__ == "__main__":
    bench_model_stats = defaultdict(dict)
    for bench in BENCHES:
        for model in MODELS:
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
            res_items = []
            if path.exists():
                with path.open() as file:
                    for line in file:
                        res_items.append(json.loads(line))

            stats = {
                "tokens": 0,
                "cost": 0,
                "score": None,
                "std": None
            }
            results = []
            for res_item in res_items:
                for key in ["total_tokens", "totalTokens"]:
                    if key in res_item["usage"]:
                        stats["tokens"] += res_item["usage"][key]
                        break
                else:
                    raise ValueError(res_item["usage"])

                stats["cost"] += res_item["model_cost"]
                results.append(res_item["is_correct"])

            if model.currency == "rub":
                stats["cost"] /= 100

            if not results:
                stats["score"] = 0
                stats["std"] = 0

            else:
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
               stats["score"] = score
               stats["std"] = (std1 + std2) / 2

            bench_model_stats[bench.id][model.id] = stats

    model_stats = {}
    for model in MODELS:
        tokens, cost = 0, 0
        scores, stds = [], []
        for bench in BENCHES:
            stats = bench_model_stats[bench.id][model.id]
            tokens += stats["tokens"]
            cost += stats["cost"]
            scores.append(stats["score"])
            stds.append(stats["std"])

        if model.client == "runpod":
            cost = RUNPOD_COSTS[model.id]

        model_stats[model.id] = {
            "name": model.name,
            "tokens": tokens,
            "cost": cost,
            "avg_score": np.mean(scores),
            "avg_std": np.sqrt(np.mean([_**2 for _ in stds]))
        }

    path = PROJ_DIR / "data" / "stats.json"
    print(f'Write "{path}"')
    with path.open("w") as file:
        data = {
            "bench_model_stats": bench_model_stats,
            "model_stats": model_stats
        }
        json.dump(data, file, indent=2)
