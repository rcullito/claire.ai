import nltk

def find_nouns(user_text):
    tokens = nltk.word_tokenize(user_text)
    parts_of_speech = nltk.pos_tag(tokens)
    nouns = [noun for (noun, pos) in parts_of_speech if pos == "NN"]
    return nouns
