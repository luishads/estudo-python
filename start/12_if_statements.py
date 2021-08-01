# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    12_if_statements.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 14:48:13 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 15:10:51 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall")
