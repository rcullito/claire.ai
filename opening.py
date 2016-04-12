import pos
import clarify

def prompt_user(indy_prompt_text):
    return raw_input(indy_prompt_text)


def get_nouns_from_user(prompt):
    response = prompt_user(prompt)
    nouns = pos.find_nouns(response)

    if not nouns:
        clarify_prompt = clarify.generate_response()
        get_nouns_from_user(clarify_prompt)

    return nouns

prompt = "You're in a pinch. Tell Indy what you need. : "
nouns = get_nouns_from_user(prompt)

### if we see the word something, analyze the block of text coming after it


print nouns
