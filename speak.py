import nltk

text = nltk.word_tokenize("And now for something completely different")

parts = nltk.pos_tag(text)

print parts
