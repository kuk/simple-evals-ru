
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
    # Bench(
    #     id="simpleqa",
    #     name="simpleqa-1k",
    #     reqs=[
    #         "openrouter",
    #     ]
    # ),
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
#  flash-1.5
#  flash-2.0
#  flash-2.0-turbo?
#  pro-1.5
# llama
# . 3.3-70b
# . 3.1-8b
# .
# mistral
#  nemo
#  ?
# qwen
#  ?
# deepseek
#  v3

# yandexgpt
#  pro
# . lite
# gigachat
#  max
#  pro
# . lite


@dataclass
class Model:
    id: str
    name: str
    client: str
    client_model: str
    currency: str = "usd"


MODELS = [
    Model(
        id="08_gigachat_lite",
        name="gigachat-lite",
        client="gigachat",
        client_model="GigaChat",
        currency="rub",
    ),

    Model(
        id="07_yandexgpt_4_lite",
        name="yandexgpt-4-lite",
        client="yandexgpt",
        client_model="yandexgpt-lite/latest",
        currency="rub",
    ),
    Model(
        id="09_yandexgpt_3_lite",
        name="yandexgpt-3-lite",
        client="yandexgpt",
        client_model="yandexgpt-lite/deprecated",
        currency="rub",
    ),

    Model(
        id="01_gemini_flash_1_5",
        name="gemini-flash-1.5",
        client="openrouter",
        client_model="google/gemini-flash-1.5",
    ),

    Model(
        id="02_llama_3_2_1b",
        name="llama-3.2-1b",
        client="openrouter",
        client_model="meta-llama/llama-3.2-1b-instruct",
    ),
    Model(
        id="03_llama_3_2_3b",
        name="llama-3.2-3b",
        client="openrouter",
        client_model="meta-llama/llama-3.2-3b-instruct",
    ),
    Model(
        id="04_llama_3_1_8b",
        name="llama-3.1-8b",
        client="openrouter",
        client_model="meta-llama/llama-3.1-8b-instruct",
    ),
    Model(
        id="10_llama_3_1_8b",
        name="llama-3.1-8b:yandex",
        client="yandexgpt",
        client_model="llama-lite/latest",
        currency="rub",
    ),
    Model(
        id="05_llama_3_3_70b",
        name="llama-3.3-70b",
        client="openrouter",
        client_model="meta-llama/llama-3.3-70b-instruct",
    ),

    Model(
        id="06_qwen_2_5_7b",
        name="qwen-2.5-7b",
        client="openrouter",
        client_model="qwen/qwen-2.5-7b-instruct",
    ),
]
