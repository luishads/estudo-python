# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess_the_number.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/01 14:56:11 by lamorim           #+#    #+#              #
#    Updated: 2021/08/01 15:37:00 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

# User gona guess the number
def guess(x):
    random_nbr = random.randint(1, x)
    guess = 0
    while guess != random_nbr:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_nbr:
            print('Sorry, guess again. Too low.')
        elif guess > random_nbr:
            print('Sorry, guess again. Too high.')

    print(f'Congrats! You have guess the number {random_nbr} correctly!')

# computer gona guess the number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could be high becouse low = high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?\n').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Computer guessed your number! Bip.')

# guess(42)
computer_guess(42)
