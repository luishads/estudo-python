# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    13_if_statements_comparisons.py                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 15:12:59 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 15:18:33 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def max_nbr(nbr0, nbr1, nbr2):
    if nbr0 >= nbr1 and nbr0 >= nbr2:
        return nbr0
    elif nbr1 >= nbr0 and nbr1 >= nbr2:
        return nbr1
    else:
        return nbr2

print(max_nbr(10, 70, 9))
