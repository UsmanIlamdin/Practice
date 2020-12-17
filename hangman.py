from list import words
import random
import string

def get_valid_word(words):
    random_word = random.choice(words)
    while ' ' in random_word or '-' in random_word:
        random_word =  random.choice(words)
    return random_word.upper()

print (get_valid_word(words))