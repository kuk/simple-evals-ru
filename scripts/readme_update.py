
import re
import sys
import json
import io
from pathlib import Path
from contextlib import contextmanager

from simple.registry import (
    MODELS,
    BENCHES
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
    with path.open() as file:
        for line in file:
            yield json.loads(line)


def print_errors_table():
    print("<table>")
    print("<tr>")
    print("<th></th>")
    for bench in BENCHES:
        print("<th>", f"{bench.name}", "</th>")
    print("</tr>")

    for model in MODELS:
        print("<tr>")
        print("<th>", model.name, "</th>")

        for bench in BENCHES:
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
            errors = sum(not _["is_correct"] for _ in load_jsonl(path))
            print(
                "<td>", f'<a href="errors/{bench.id}/{model.id}.md">',
                errors,
                "</a>", "</td>"
            )
        print("</tr>")
    print("</table>")


def print_cov_table():
    print("<table>")
    print("<tr>")
    print("<th></th>")
    for bench in BENCHES:
        path = PROJ_DIR / "data" / "benches" / f"{bench.id}.jsonl"
        total = sum(1 for _ in load_jsonl(path))
        print("<th>", f"{bench.name}, {total}", "</th>")
    print("</tr>")

    for model in MODELS:
        print("<tr>")
        print("<th>", model.name, "</th>")

        for bench in BENCHES:
            path = PROJ_DIR / "data" / "results" / bench.id / f"{model.id}.jsonl"
            cov, cost = 0, 0
            for item in load_jsonl(path):
                cov += 1
                cost += item["model_cost"]

            if model.currency == "rub":
                cost /= 100

            symbol = "$"
            if cost < 1:
                cost *= 100
                symbol = "¢"

            print("<td>", f"{cov} / {cost:.1f}{symbol}", "</td>")
        print("</tr>")
    print("</table>")


def replace_section(text, section_id, section_text):
    return re.sub(
            r'(<section id="%s">)(.*?)(</section>)' % section_id,
            r"\1%s\3" % section_text, text,
            flags=re.DOTALL
    )


if __name__ == "__main__":
    path = PROJ_DIR / "README.md"
    text = path.read_text()

    for section_name, print_func in [
            ("errors-table", print_errors_table),
            ("cov-table", print_cov_table)
    ]:

        file = io.StringIO()
        with print_to(file):
            print_func()

        assert section_name in text, section_name
        text = replace_section(text, section_name, file.getvalue())

    path.write_text(text)
