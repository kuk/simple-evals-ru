
import re


def humaneval_instruction(prompt):
    return """Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
%s""" % prompt


def humaneval_answer_pred(answer):
    chunks = re.findall(r"```(?:python)?(.+?)```", answer, flags=re.DOTALL)
    if not chunks:
        return answer
    return chunks[0]


async def humaneval_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = humaneval_instruction(task_item["prompt"])
    response = await model_client(
        instruction=res_item["instruction"]
    )
    res_item["answer"] = response["answer"]
    res_item["usage"] = response["usage"]
    res_item["model_cost"] = response["cost"]

    res_item["pred"] = humaneval_answer_pred(response["answer"])

    response = await context["e2b"](code=f"""
{task_item["prompt"]}
{res_item["pred"]}

{task_item["test"]}

check({task_item["entry_point"]})
""")

    res_item["traceback"] = response["traceback"]
    res_item["timed_out"] = response["timed_out"]
    res_item["is_correct"] = (
        not res_item["traceback"]
        and not res_item["timed_out"]
    )
    res_item["bench_cost"] = response["cost"]
