
CAT_MULTICHOICE_TARGETS = {
    "boolean_expressions": ["False", "True"],
    "causal_judgement": ["No", "Yes"],
    "date_understanding": ["(A)", "(B)", "(C)", "(D)", "(E)", "(F)"],
    "disambiguation_qa": ["(A)", "(B)", "(C)"],
    "formal_fallacies": ["invalid", "valid"],
    "geometric_shapes": ["(A)", "(B)", "(C)","(D)", "(E)", "(F)", "(G)", "(I)", "(J)", "(K)"],
    "hyperbaton": ["(A)", "(B)"],
    "logical_deduction_five_objects": ["(A)", "(B)", "(C)", "(D)", "(E)"],
    "logical_deduction_seven_objects": ["(A)", "(B)", "(C)", "(D)", "(E)", "(F)", "(G)"],
    "logical_deduction_three_objects": ["(A)", "(B)", "(C)"],
    "movie_recommendation": ["(A)", "(B)", "(C)", "(D)", "(E)"],
    "navigate": ["No", "Yes"],
    "penguins_in_a_table": ["(A)", "(B)", "(C)", "(D)", "(E)"],
    "reasoning_about_colored_objects": ["(A)", "(B)", "(C)", "(D)", "(E)", "(F)", "(G)", "(H)", "(I)", "(J)", "(K)", "(L)", "(M)", "(N)", "(O)", "(P)", "(Q)", "(R)"],
    "ruin_names": ["(A)", "(B)", "(C)", "(D)"],
    "salient_translation_error_detection": ["(A)", "(B)", "(C)", "(D)", "(E)", "(F)"],
    "snarks": ["(A)", "(B)"],
    "sports_understanding": ["no", "yes"],
    "temporal_sequences": ["(A)", "(B)", "(C)", "(D)"],
    "tracking_shuffled_objects_five_objects": ["(A)", "(B)", "(C)", "(D)", "(E)"],
    "tracking_shuffled_objects_seven_objects": ["(A)", "(B)", "(C)", "(D)", "(E)", "(F)", "(G)"],
    "tracking_shuffled_objects_three_objects": ["(A)", "(B)", "(C)"],
    "web_of_lies": ["No", "Yes"],
}

CAT_OTHER_TARGET_CONSTRAINS = {
    "dyck_languages": 'Respond with space separated symbols ")", ">", "}", "]"; example responses include ") ) >", ">", "} } ] >"',
    "multistep_arithmetic_two": "Respond with an integer",
    "object_counting": "Respond with a positive integer",
    "word_sorting": "Respond with space separated lowercase words"
}


def bbh_instruction(cat, input_, cat_prompts):
    cot_prompt = cat_prompts[cat]
    assert "Q: " in cot_prompt, cot_prompt
    assert "A: " in cot_prompt, cot_prompt
    return f"""{cot_prompt}

Q: {input_}"""


def bbh_postproc_instruction(cat, answer):
    assert cat in CAT_MULTICHOICE_TARGETS or cat in CAT_OTHER_TARGET_CONSTRAINS, cat
    if cat in CAT_MULTICHOICE_TARGETS:
        constrain = "Responde with one of: %s" % ", ".join('"%s"' % _ for _ in CAT_MULTICHOICE_TARGETS[cat])
    elif cat in CAT_OTHER_TARGET_CONSTRAINS:
        constrain = CAT_OTHER_TARGET_CONSTRAINS[cat]

    return f"""Given the solution to question, your task is to extract the final answer.
{constrain}. In case you cannot find a final answer, respond with "?".

----

{answer}"""


async def bbh_worker(model_client, task_item, res_item, context):
    res_item["instruction"] = bbh_instruction(
        task_item["cat"], task_item["input"],
        context["bbh_prompts"]
    )
    response = await model_client(instruction=res_item["instruction"])
    res_item["answer"] = response["answer"]
    res_item["model_cost"] = response["cost"]

    response = await context["openrouter"](
        model="google/gemini-flash-1.5",
        instruction=bbh_postproc_instruction(task_item["cat"], res_item["answer"])
    )
    res_item["pred"] = response["answer"].strip()
    res_item["is_correct"] = res_item["pred"] == task_item["target"]
    res_item["bench_cost"] = response["cost"]

