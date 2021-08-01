# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    17_guessing_game.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 15:55:31 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 16:08:55 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

secret_word = "na"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose!")
else:
    print("You win!")
