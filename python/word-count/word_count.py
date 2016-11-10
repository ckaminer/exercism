import string

def word_count(sentence):
    clean = sanitize_sentence(sentence)
    words = clean.split()
    counter = {}
    for word in words:
        if word.lower() in counter.keys():
            counter[word.lower()] += 1
        else:
            counter[word.lower()] = 1
    return counter

def sanitize_sentence(sentence):
    for c in string.punctuation:
        sentence = sentence.replace(c, " ")
    return sentence
