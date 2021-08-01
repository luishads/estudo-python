# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    21_build_a_translator.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 18:19:55 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 18:33:18 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
