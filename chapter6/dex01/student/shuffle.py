import random

def shuffleString(theString):
    chars = list(theString)
    random.shuffle(chars)
    return "".join(chars)

print(shuffleString("Apples are red"))