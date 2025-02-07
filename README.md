
# simple-evals-ru

```
mkdir -p data/cache/mgsm
curl -o data/cache/mgsm/mgsm_en.tsv https://openaipublic.blob.core.windows.net/simple-evals/mgsm_en.tsv
uv run scripts/tasks/mgsm.py data/cache/mgsm/mgsm_en.tsv data/tasks/gsm8k.json
head data/tasks/gsm8k.json

mkdir -p data/cache/math
curl -o data/cache/math/math_test.csv https://openaipublic.blob.core.windows.net/simple-evals/math_test.csv
curl -o data/cache/math/math_500_test.csv https://openaipublic.blob.core.windows.net/simple-evals/math_500_test.csv
uv run scripts/tasks/math_.py data/cache/math/math_test.csv data/cache/math/math_500_test.csv data/tasks/math.json
head data/tasks/math.json

```

```
export NO_COLOR=1
export PATH=/opt/homebrew/bin:$PATH
. ~/proj/simple-evals-ru/.envrc
uv run ruff check ~/proj/simple-evals-ru/scripts/tasks/*.py

```
