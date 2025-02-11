
def mmlu_instruction(question, options):
    return f"""Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering.

{question}

A) {options["A"]}
B) {options["B"]}
C) {options["C"]}
D) {options["D"]}
E) {options["E"]}
F) {options["F"]}
G) {options["G"]}
H) {options["H"]}
I) {options["I"]}
J) {options["J"]}"""


def mmlu_postproc_instruction(answer):
    return f"""Given the solution to multiple choice exam question, your task is to extract the final answer. Respond with a single letter: A|B|C|D|E|F|G|H|I|J. In case you cannot find a single letter final answer, respond with "?"

----

{answer}"""


async def mmlu_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = mmlu_instruction(task_item["question"], task_item["options"])
    response = await model_client(instruction=res_item["instruction"])
    res_item["answer"] = response["answer"]
    res_item["usage"] = response["usage"]
    res_item["model_cost"] = response["cost"]

    response = await context["openrouter"](
        model="google/gemini-flash-1.5",
        instruction=mmlu_postproc_instruction(res_item["answer"])
    )
    res_item["pred"] = response["answer"].strip()
    res_item["is_correct"] = res_item["pred"] == task_item["target"]
    res_item["bench_cost"] = response["cost"]
