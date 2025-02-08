
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
uv run scripts/tasks/mmlu.py data/cache/mmlu/test-00000-of-00001.parquet data/tasks/mmlu_pro_sample.json
head data/tasks/mmlu_pro_sample.json

mkdir -p data/cache/simpleqa
curl -L -o data/cache/simpleqa/simple_qa_test_set.csv https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv 
uv run scripts/tasks/simpleqa.py data/cache/simpleqa/simple_qa_test_set.csv data/tasks/simpleqa_sample.json
head data/tasks/simpleqa_sample.json

mkdir -p data/cache/bbh
curl -L -o data/cache/bbh/main.zip https://github.com/suzgunmirac/BIG-Bench-Hard/archive/refs/heads/main.zip
unzip -d data/cache/bbh data/cache/bbh/main.zip
uv run scripts/tasks/bbh.py data/cache/bbh/BIG-Bench-Hard-main/bbh data/cache/bbh/BIG-Bench-Hard-main/cot-prompts data/tasks/bbh_sample.json data/tasks/bbh_prompts.json
head data/tasks/bbh_sample.json
```

```
export NO_COLOR=1
export PATH=/opt/homebrew/bin:$PATH
PROJ=~/proj/simple-evals-ru
. $PROJ/.envrc
uv run ruff check $PROJ/main.py $(find $PROJ/simple $PROJ/scripts $PROJ/tests -name '*.py')
uv run pytest -s $PROJ/tests/*.py
```
