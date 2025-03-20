
import re
import sys
import json
import io
from pathlib import Path
from contextlib import contextmanager
from collections import Counter

from simple.registry import (
    MODELS,
    BENCHES,
)


CUR_DIR = Path(__file__).parent
PROJ_DIR = CUR_DIR.parent


@contextmanager
def print_to(file):
    orig_stdout = sys.stdout
    try:
        sys.stdout = file
        yield
    finally:
        sys.stdout = orig_stdout


def load_jsonl(path):
    items = []
    with path.open() as file:
        for line in file:
            items.append(json.loads(line))
    return items


def nb(string):
    return (
        string
        .replace(" ", "&nbsp;")
        .replace("-", "&#8209;")
    )


def print_scores_table(stats_data, _, __):
    print("<table>")
    print("<tr>")
    print("<th></th>")
    print("<th>$ / m tokens</th>")
    print("<th>avg</th>")
    for bench in BENCHES:
        print("<th>", nb(bench.name), "</th>")
    print("<th></th>")
    print("</tr>")

    for model in MODELS:
        stats = stats_data["model_stats"][model.id]

        print("<tr>")
        print("<th>", nb(model.name), "</th>")

        if model.client == "runpod":
            print("<td>selfhost</td>")

        else:
            cost = stats["cost"] / stats["tokens"] * 1_000_000
            print(f"<td>${cost:.2f}</td>")

        print(f'<td>{stats["avg_score"] * 100:.1f}±{stats["avg_std"] * 100:.1f}%</td>')

        for bench in BENCHES:
            stats = stats_data["bench_model_stats"][bench.id][model.id]
            print(f'<td>{stats["score"] * 100:.1f}±{stats["std"] * 100:.1f}%</td>')

        print("<th>", nb(model.name), "</th>")
        print("</tr>")
    print("</table>")


def print_results_table(_, bench_task_items, bench_model_res_items):
    print("<table>")
    print("<tr>")
    print("<th></th>")
    for bench in BENCHES:
        print(
            "<th>",
            nb(bench.name),
            "<br/>",
            len(bench_task_items[bench.id]),
            "</th>"
        )
    print("<th></th>")
    print("</tr>")

    for model in MODELS:
        print("<tr>")
        print("<th>", nb(model.name), "</th>")

        for bench in BENCHES:
            counts = Counter()
            for res_item in bench_model_res_items[bench.id, model.id]:
                counts[res_item["is_correct"]] += 1

            print(
                "<td>",
                f'<a href="reports/correct/{bench.id}/{model.id}.md">',
                counts[True], "✓", "</a>",
                "/",
                f'<a href="reports/errors/{bench.id}/{model.id}.md">',
                counts[False], "✗"
                "</a>",
                "</td>",
                sep="&nbsp;"
            )

        print("<th>", nb(model.name), "</th>")
        print("</tr>")
    print("</table>")


def print_cov_table(_, bench_task_items, bench_model_res_items):
    print("<table>")
    print("<tr>")
    print("<th></th>")
    for bench in BENCHES:
        print(
            "<th>",
            nb(bench.name),
            "<br/>",
            len(bench_task_items[bench.id]),
            "</th>"
        )
    print("</tr>")

    for model in MODELS:
        print("<tr>")
        print("<th>", nb(model.name), "</th>")

        for bench in BENCHES:
            cov, cost = 0, 0
            for res_item in bench_model_res_items[bench.id, model.id]:
                cov += 1
                cost += res_item["model_cost"]

            if model.currency == "rub":
                cost /= 100

            if model.client == "runpod":
                cost = 0

            print(
                "<td>",
                nb(f"{cov} / {cost:.1f}$"),
                "</td>"
            )
        print("</tr>")
    print("</table>")


def replace_section(text, section_id, section_text):
    return re.sub(
            r'(<section id="%s">)(.*?)(</section>)' % section_id,
            r"\1%s\3" % section_text, text,
            flags=re.DOTALL
    )


if __name__ == "__main__":
    bench_task_items = {}
    for bench in BENCHES:
        path = PROJ_DIR / "data" / "benches" / f"{bench.id}.jsonl"
        assert path.exists(), path
        bench_task_items[bench.id] = load_jsonl(path)

    bench_model_res_items = {}
    for bench in BENCHES:
        for model in MODELS:
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
            res_items = []
            if path.exists():
                res_items = load_jsonl(path)
            bench_model_res_items[bench.id, model.id] = res_items

    path = PROJ_DIR / "data" / "stats.json"
    with path.open() as file:
        stats_data = json.load(file)

    path = PROJ_DIR / "README.md"
    text = path.read_text()

    for section_name, print_func in [
            ("scores-table", print_scores_table),
            ("results-table", print_results_table),
            ("cov-table", print_cov_table)
    ]:
        file = io.StringIO()
        with print_to(file):
            print_func(stats_data, bench_task_items, bench_model_res_items)

        assert section_name in text, section_name
        text = replace_section(text, section_name, file.getvalue())

    print(f'Write "{path}"')
    path.write_text(text)
