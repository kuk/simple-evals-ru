

def humaneval_instruction(prompt):
    return """Read the following function signature and docstring, and fully implement the function described. Your response should only contain the code for this function.
%s""" % prompt


def humaneval_postproc_instruction(answer, entry_point):
    return f"""From input text extract the function "{entry_point}" body lines. Respond only with function body lines, do not add ```. You response should be a substring of input text, keep the original indentation. In case the function is not found responde with empty string.

Example input:
```python
def all_prefixes(string: str) -> List[str]:
    ''' Return list of all prefixes from shortest to longest of the input string
    '''
    return [string[:i] for i in range(1, len(string) + 1)]
```

Output:
    return [string[:i] for i in range(1, len(string) + 1)]


----

Input text is inside ```:

```
{answer}
```"""


async def humaneval_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = humaneval_instruction(task_item["prompt"])
    response = await model_client(
        instruction=res_item["instruction"]
    )
    res_item["answer"] = response["answer"]
    res_item["model_cost"] = response["cost"]

    response = await context["openrouter"](
        model="google/gemini-flash-1.5",
        instruction=humaneval_postproc_instruction(
            res_item["answer"], task_item["entry_point"])
    )
    res_item["pred"] = response["answer"]
    res_item["bench_cost"] = response["cost"]

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
    res_item["bench_cost"] += response["cost"]
