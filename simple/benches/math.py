

def math_instruction(problem):
    return """Solve the following math problem step by step. The last line of your response should be of the form Answer: $ANSWER (without quotes) where $ANSWER is the answer to the problem.

%s

Remember to put your answer on its own line after "Answer:", and you do not need to use a \\boxed command""" % problem


def math_postproc_instruction(answer):
    return """Given the solution to math problem extract the final answer.

Examples

Solution: ... The final answer is: $\boxed{(8, -2)}$
Answer: (8, -2)

-----

YOUR TASK

The solution text is given in ```. Respond only with the final answer. You response should be a substring of solution text. In case you cannot find a final answer in given text, respond with "?".

```
%s
```""" % answer


def math_judge_instruction(pred, target):
    return """Look at the following two expressions (answers to a math problem) and judge whether they are equivalent. Only perform trivial simplifications

Examples:

    Expression 1: $2x+3$
    Expression 2: $3+2x$

Yes

    Expression 1: 3/2
    Expression 2: 1.5

Yes

    Expression 1: $x^2+2x+1$
    Expression 2: $y^2+2y+1$

No

    Expression 1: $x^2+2x+1$
    Expression 2: $(x+1)^2$

Yes

    Expression 1: 5
    Expression 2: x=5

Yes

    Expression 1: 3245/5
    Expression 2: 649

No
(these are actually equal, don't mark them equivalent if you need to do nontrivial simplifications)

    Expression 1: 2/(-3)
    Expression 2: -2/3

Yes
(trivial simplifications are allowed)

    Expression 1: 72 degrees
    Expression 2: 72

Yes
(give benefit of the doubt to units)

    Expression 1: 64
    Expression 2: 64 square feet

Yes
(give benefit of the doubt to units)

---

YOUR TASK


Respond with only "Yes" or "No" (without quotes). Do not include a rationale.

    Expression 1: %s
    Expression 2: %s""" % (pred, target)



async def math_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = math_instruction(task_item["problem"])
    response = await model_client(instruction=res_item["instruction"])
    res_item["answer"] = response["answer"]
    res_item["usage"] = response["usage"]
    res_item["model_cost"] = response["cost"]

    response = await context["openrouter"](
        model="google/gemini-flash-1.5",
        instruction=math_postproc_instruction(res_item["answer"])
    )
    res_item["pred"] = response["answer"].strip()
    res_item["bench_cost"] = response["cost"]

    response = await context["openrouter"](
        model="google/gemini-flash-1.5",
        instruction=math_judge_instruction(res_item["pred"], task_item["target"])
    )
    res_item["is_correct"] = response["answer"].strip() == "Yes"
    res_item["bench_cost"] += response["cost"]

