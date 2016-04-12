import pos
import clarify

def prompt_user(indy_prompt_text):
    return raw_input(indy_prompt_text).lower()

def get_nouns_from_user(prompt):
    response = prompt_user(prompt)
    nouns = pos.find_nouns(response)

    if not nouns:
        clarify_prompt = clarify.generate_response()
        get_nouns_from_user(clarify_prompt)

    return {
        'nouns': nouns,
        'response': response
    }

prompt = "You're in a pinch. Tell Indy what you need. : "
initial_feedback = get_nouns_from_user(prompt)

if 'something' in initial_feedback.get('nouns'):
    clarify.find_something_from(initial_feedback.get('response'))
