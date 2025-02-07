
# simple-evals-ru

```
mkdir -p data/cache/mgsm
curl -o data/cache/mgsm/mgsm_ru.tsv https://openaipublic.blob.core.windows.net/simple-evals/mgsm_ru.tsv
uv run scripts/tasks/mgsm.py data/cache/mgsm/mgsm_ru.tsv data/tasks/mgsm_ru.json
head data/tasks/mgsm_ru.json

mkdir -p data/cache/math
curl -o data/cache/math/math_test.csv https://openaipublic.blob.core.windows.net/simple-evals/math_test.csv
curl -o data/cache/math/math_500_test.csv https://openaipublic.blob.core.windows.net/simple-evals/math_500_test.csv
uv run scripts/tasks/math_500.py data/cache/math/math_test.csv data/cache/math/math_500_test.csv data/tasks/math_500.json
head data/tasks/math_500.json

mkdir -p data/cache/humaneval
curl -L -o data/cache/humaneval/HumanEval.jsonl.gz https://github.com/openai/human-eval/raw/refs/heads/master/data/HumanEval.jsonl.gz
gunzip data/cache/humaneval/HumanEval.jsonl.gz
uv run scripts/tasks/humaneval.py data/cache/humaneval/HumanEval.jsonl data/tasks/humaneval.json
head data/tasks/humaneval.json

mkdir -p data/cache/mmlu
curl -L -o data/cache/mmlu/test-00000-of-00001.parquet https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/resolve/main/data/test-00000-of-00001.parquet
uv run scripts/tasks/mmlu.py data/cache/mmlu/test-00000-of-00001.parquet data/tasks/mmlu_pro_mini.json
head data/tasks/mmlu_pro_mini.json
```

```
export NO_COLOR=1
export PATH=/opt/homebrew/bin:$PATH
. ~/proj/simple-evals-ru/.envrc
uv run ruff check ~/proj/simple-evals-ru/scripts/tasks/*.py

```
