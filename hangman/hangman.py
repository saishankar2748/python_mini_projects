import random
import string
from words import words

def is_valid_word(somet):
    
    word = random.choice(somet)
    while "-" in word or ' ' in word:
        word = random.choice(somet)
        
    return word.upper()

def hangman():
    
    word = is_valid_word(words)
    word_letter = set(word)   # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letter) > 0 and lives > 0:

        print('You have',lives, 'lives left and you have guessed these letters : ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('current word : ',' '.join(word_list))


        user_letter = input('Enter a letter :').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives -1

        elif user_letter in used_letters:
            print("You have literally just guessed that letter ")

        else :
            print('Invalid letter')   
        
    if lives==0:
        print('You died, sorry. The word was ',word)
    else:
        print('Yay!! You guessed the word',word, '!!')


hangman()