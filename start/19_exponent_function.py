# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    19_exponent_function.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 16:29:06 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 17:23:06 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(raise_to_power(5, 3))
