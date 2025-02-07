
# simple-evals-ru

```
mkdir -p data/cache/mgsm
curl -o data/cache/mgsm/mgsm_en.tsv https://openaipublic.blob.core.windows.net/simple-evals/mgsm_en.tsv
uv run scripts/tasks/mgsm.py data/cache/mgsm/mgsm_en.tsv data/tasks/gsm8k.json
head data/tasks/gsm8k.json


```

```
export NO_COLOR=1
export PATH=/opt/homebrew/bin:$PATH
. ~/proj/simple-evals-ru/.envrc
uv run ruff check ~/proj/simple-evals-ru/scripts/tasks/*.py

```
