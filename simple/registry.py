
import os
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
        reqs=[
            "openrouter",
        ]
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
# . flash-1.5
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
# . 2.5-7b
#  2.5-14b
#  2.5-72b
# deepseek
#  v3

# yandexgpt
# . pro
# . lite
# gigachat
# . max
# . pro
# . lite


@dataclass
class Model:
    id: str
    name: str
    client: str
    client_model: str
    client_endpoint_id: str = None
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
        id="12_gigachat_pro",
        name="gigachat-pro",
        client="gigachat",
        client_model="GigaChat-Pro",
        currency="rub",
    ),
    Model(
        id="14_gigachat_max",
        name="gigachat-max",
        client="gigachat",
        client_model="GigaChat-Max",
        currency="rub",
    ),

    Model(
        id="07_yandexgpt_4_lite",
        name="yandexgpt-4-lite",
        client="yandexgpt",
        client_model="yandexgpt-lite/latest",
        currency="rub",
    ),
    # Model(
    #     id="09_yandexgpt_3_lite",
    #     name="yandexgpt-3-lite",
    #     client="yandexgpt",
    #     client_model="yandexgpt-lite/deprecated",
    #     currency="rub",
    # ),
    Model(
        id="11_yandexgpt_4_pro",
        name="yandexgpt-4-pro",
        client="yandexgpt",
        client_model="yandexgpt/latest",
        currency="rub",
    ),
    Model(
        id="17_yandexgpt_5_pro",
        name="yandexgpt-5-pro",
        client="yandexgpt",
        client_model="yandexgpt/rc",
        currency="rub",
    ),

    # Model(
    #     id="18_cotype_nano",
    #     name="cotype-nano",
    #     client="runpod",
    #     client_model="MTSAIR/Cotype-Nano",
    #     client_endpoint_id=os.getenv("RUNPOD_ENDPOINT1")
    # ),

    # Model(
    #     id="19_t_lite",
    #     name="t-lite",
    #     client="runpod",
    #     client_model="t-tech/T-lite-it-1.0",
    #     client_endpoint_id=os.getenv("RUNPOD_ENDPOINT2")
    # ),
    Model(
        id="20_t_pro",
        name="t-pro",
        client="runpod",
        client_model="t-tech/T-pro-it-1.0",
        client_endpoint_id=os.getenv("RUNPOD_ENDPOINT3")
    ),

    # Model(
    #     id="01_gemini_flash_1_5",
    #     name="gemini-flash-1.5",
    #     client="openrouter",
    #     client_model="google/gemini-flash-1.5",
    # ),

    # Model(
    #     id="02_llama_3_2_1b",
    #     name="llama-3.2-1b",
    #     client="openrouter",
    #     client_model="meta-llama/llama-3.2-1b-instruct",
    # ),
    # Model(
    #     id="03_llama_3_2_3b",
    #     name="llama-3.2-3b",
    #     client="openrouter",
    #     client_model="meta-llama/llama-3.2-3b-instruct",
    # ),
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
        id="13_llama_3_3_70b",
        name="llama-3.3-70b:yandex",
        client="yandexgpt",
        client_model="llama/latest",
        currency="rub",
    ),

    # Model(
    #     id="06_qwen_2_5_7b",
    #     name="qwen-2.5-7b",
    #     client="openrouter",
    #     client_model="qwen/qwen-2.5-7b-instruct",
    # ),
    Model(
        id="15_qwen_2_5_72b",
        name="qwen-2.5-72b",
        client="openrouter",
        client_model="qwen/qwen-2.5-72b-instruct",
    ),

    Model(
        id="16_deepseek_v3",
        name="deepseek-v3",
        client="openrouter",
        client_model="deepseek/deepseek-chat",
    ),
]
