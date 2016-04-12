import random

clarify_prompts = [
    "Sorry, Indy didn't catch that. Can you try rephrasing your question? : ",
    "We couldn't figure out what you mean. Out with it partner! : ",
    "You're going to have to do better than that. : "
]

def generate_response():
    return random.choice(clarify_prompts)
