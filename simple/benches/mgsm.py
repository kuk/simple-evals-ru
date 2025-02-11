
import re


def mgsm_instruction(problem):
    return """Solve this math problem. Give the reasoning steps before giving the final answer on the last line by itself in the format of "Answer:". Do not add anything other than the integer answer after "Answer:".

%s""" % problem


def mgsm_answer_pred(answer):
    matches = list(re.finditer(r"(Answer|Ответ)", answer))
    if not matches:
        return

    match = matches[-1]
    suffix = answer[match.end():]

    match = re.search(r"(\d+[.,]?\d*)", suffix)
    if not match:
        return

    return int(re.sub(r"[,.]", "", match.group(1)))


async def mgsm_worker(model_client, task_item, res_item, _):
    res_item["instruction"] = mgsm_instruction(task_item["problem"])
    response = await model_client(instruction=res_item["instruction"])
    res_item["answer"] = response["answer"]
    res_item["usage"] = response["usage"]
    res_item["model_cost"] = response["cost"]

    res_item["pred"] = mgsm_answer_pred(res_item["answer"])
    res_item["is_correct"] = res_item["pred"] == task_item["target"]
    res_item["bench_cost"] = 0
