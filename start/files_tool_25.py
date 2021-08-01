# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    files_tool_25.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 21:17:14 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 21:17:19 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

feet_in_mile = 5280
maters_in_kilometer = 1000
beatles = [
        "John Lennon",
        "Paul McCartney",
        "George Harrison",
        "Ringo Star"
        ]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(nbr):
    return random.randint(1, nbr)
