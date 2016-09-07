
def to_rna(strand):
    pairs = {"G": "C", "C": "G", "T": "A", "A": "U"}
    result = ""
    for letter in strand:
        result += pairs[letter]
    return result
