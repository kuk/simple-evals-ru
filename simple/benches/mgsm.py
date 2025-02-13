

def mgsm_instruction(problem):
    return """Solve this math problem. Give the reasoning steps before giving the final answer on the last line by itself in the format of "Answer:". Do not add anything other than the integer answer after "Answer:".

%s""" % problem


def mgsm_postproc_instruction(answer):
    return """Given the solution to math problem extract the final answer. Respond with a number. In case you cannot find a final answer in given text, or the final answer is not a number, respond with "?".

---

%s""" % answer


async def mgsm_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = mgsm_instruction(task_item["problem"])
    response = await model_client(instruction=res_item["instruction"])
    res_item["answer"] = response["answer"]
    res_item["usage"] = response["usage"]
    res_item["model_cost"] = response["cost"]

    response = await context["openrouter"](
        model="google/gemini-flash-1.5",
        instruction=mgsm_postproc_instruction(res_item["answer"])
    )
    res_item["pred"] = (
        response["answer"].strip()
        .replace(",", ".")
        .removesuffix(".00")
    )
    res_item["bench_cost"] = response["cost"]
    res_item["is_correct"] = res_item["pred"] == task_item["target"]
