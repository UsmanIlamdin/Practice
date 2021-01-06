from list import words
import random
import string

def get_valid_word(words):
    random_word = random.choice(words)
    while ' ' in random_word or '-' in random_word:
        random_word =  random.choice(words)
    return random_word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    live = 10
    while len(word_letters) > 0 and live > 0:

        print(f'You have{live} lives left and choose these word',' '.join(used_letters))

         # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                print('You letter,', user_letter, 'not in word!')
                live -= 1 
        elif user_letter in word_letters:
            live -= 1 
            print(f'You have used this letter {user_letter}')
        else:
            live -= 1
            print('This is not valid letter')
        

    if live ==0:
        print(f'ooh! you are out of move')
    else:
        print(f'YAY! you won the game and letter is {word}')


hangman()