
from dataclasses import dataclass


@dataclass
class Bench:
    id: str
    name: str
    reqs: [str]


BENCHES = [
    Bench(
        id="mgsm",
        name="mgsm-en",
        reqs=[]
    ),
    Bench(
        id="math",
        name="math-500",
        reqs=[
            "openrouter",
        ]
    ),
    Bench(
        id="humaneval",
        name="humaneval",
        reqs=[
            "openrouter",
            "e2b"
        ]
    ),
    Bench(
        id="mmlu",
        name="mmlu-pro-1k",
        reqs=[
            "openrouter",
        ]
    ),
    Bench(
        id="simpleqa",
        name="simpleqa-1k",
        reqs=[
            "openrouter",
        ]
    ),
    Bench(
        id="bbh",
        name="bbh-1k",
        reqs=[
            "openrouter",
            "bbh_prompts"
        ]
    ),

]

# openai
#  4o
#  4o-mini
# anthropic
#  sonnet-3.5
#  haiku-3.5
# gemini
#  flash-2.0
#  pro-1.5
# llama
#  3.3-70b
#  3.1-8b
#  ?
# mistral
#  nemo
#  ?
# qwen
#  ?
# deepseek
#  v3

# yandexgpt
#  pro
#  lite
# gigachat
#  max
#  pro
#  lite


@dataclass
class Model:
    id: str
    name: str
    client: str
    client_model: str


MODELS = [
    Model(
        id="01_gemini_flash_1_5",
        name="gemini-flash-1.5",
        client="openrouter",
        client_model="google/gemini-flash-1.5",
    ),

    # Model(
    #     id="",
    #     name="yandexgpt-4-lite",
    #     client="yandexgpt",
    #     client_model="yandexgpt-lite/latest",
    # ),
    # Model(
    #     id="",
    #     name="gigachat-lite",
    #     client="gigachat",
    #     client_model="GigaChat"
    # )
]

# meta-llama/llama-3.2-1b-instruct
# meta-llama/llama-3.2-3b-instruct
# meta-llama/llama-3.1-8b-instruct
# meta-llama/llama-3.3-70b-instruct
# qwen/qwen-2.5-7b-instruct
