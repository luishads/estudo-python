# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rock_paper_scissors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/01 16:16:50 by lamorim           #+#    #+#              #
#    Updated: 2021/08/01 16:31:00 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissors:\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a tie"

    if user_win(user, computer):
        return 'You won!'

    return 'You lost!'

def user_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
        (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
            return True

print(play())
