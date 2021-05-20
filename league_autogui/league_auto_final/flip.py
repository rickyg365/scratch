
"""
Code Wars Excercise

Author: RickyG3

"""

# I was getting this wrong because I didnt read the prompt carefully,
# it said to only invert words that have more than 5 letters
def spin_words(sentence):
    # Your code goes here
    new_sentence = []

    raw_words = sentence.split(' ')

    for word in raw_words:
        new_word = word[::-1]
        new_sentence.append(new_word)
    new_sentence = " ".join(new_sentence)

    return new_sentence

# # A clever solution from the codewars website
# import re
#
# def spin_words(sentence):
#     # Your code goes here
#     return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)


if __name__ == "__main__":
    # sentence = "Hi you fucking asshole"
    sentence = "to the stars and beyond"
    print(spin_words(sentence))
