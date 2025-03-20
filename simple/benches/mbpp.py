
import re


def mbpp_instruction(prompt, test, signature):
    return f"""Read the following instruction and fully implement the function described.

{prompt}

Your code should pass these tests:

{test}

Your response should only contain the code for this function.

{signature}
    ...


"""


def mbpp_answer_pred(answer):
    chunks = re.findall(r"```(?:python)?(.+?)```", answer, flags=re.DOTALL)
    if not chunks:
        return answer
    return chunks[0]


async def mbpp_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = mbpp_instruction(
        task_item["prompt"],
        task_item["test"],
        task_item["signature"]
    )
    response = await model_client(
        instruction=res_item["instruction"]
    )
    res_item["answer"] = response["answer"]
    res_item["usage"] = response["usage"]
    res_item["model_cost"] = response["cost"]

    res_item["pred"] = mbpp_answer_pred(response["answer"])

    response = await context["e2b"](code=f"""
{task_item["signature"]}
    ...

{res_item["pred"]}

{task_item["test"]}
""")

    res_item["traceback"] = response["traceback"]
    res_item["timed_out"] = response["timed_out"]
    res_item["is_correct"] = (
        not res_item["traceback"]
        and not res_item["timed_out"]
    )
    res_item["bench_cost"] = response["cost"]
