

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    clean = ''.join([i for i in sentence if i.isalpha()]).lower()
    for char in alphabet:
        if char not in clean:
            return False
    return True
