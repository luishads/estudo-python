# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 04:11:11 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 04:11:12 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("New\nline")
print("This \"work\" \good")
print("\tTest")

phrase = "Look the Power"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper()) # = True
print(len(phrase)) # = 14
print(phrase[0]) # = L
print(phrase.index("L")) # = 0
print(phrase.replace("Look", "See"))
