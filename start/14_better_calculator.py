# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    14_better_calculator.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 15:20:22 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 15:27:51 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

nbr0 = float(input("Enter firts number: "))
op = input("Enter operator: ")
nbr1 = float(input("Enter second number: "))

if op == "+":
    print(nbr0 + nbr1)
elif op == "-":
    print(nbr0 - nbr1)
elif op == "*":
    print(nbr0 * nbr1)
elif op == "/":
    print(nbr0 / nbr1)
else:
    print("Invalid operator")

