import nltk

text = nltk.word_tokenize("I want to borrow a bike")

parts_of_speech = nltk.pos_tag(text)

nouns = [noun for (noun, pos) in parts_of_speech if pos == "NN"]

print nouns
