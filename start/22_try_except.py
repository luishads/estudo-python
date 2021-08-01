# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    22_try_except.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 18:55:36 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 20:12:17 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    test_except = 10 / 0
    nbr = int(input("Enter a number: "))
    print(nbr)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
