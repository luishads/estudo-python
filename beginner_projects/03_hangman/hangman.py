# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hangman.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/01 16:58:19 by lamorim           #+#    #+#              #
#    Updated: 2021/08/01 18:16:57 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hungman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # user input
    while len(word_letters) > 0 and lives > 0:
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives,'lives left and you have used this letters: ', ' '.join(used_letters))

        letter_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(letter_list))

        user_letter = input('Gues a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word.")
    
        elif user_letter in used_letters:
            print("You have already used that character. Please try agian.")
    
        else:
            print("Invalid character. Please try agian.")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print('You guessed the word', word, '!!')

hungman()
