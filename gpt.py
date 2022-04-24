import openai
from interface import api_key

openai.api_key = api_key


def gpt_3(message, temp, prompt):
    return openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt(message),
        temperature=temp,
        max_tokens=100

    ).choices[0].text


def gpt_3_classification(message, labels, examples):
    return openai.Classification.create(
        search_model="ada",
        model="curie",
        examples=examples,
        query=message,
        labels=labels,
    ).label
