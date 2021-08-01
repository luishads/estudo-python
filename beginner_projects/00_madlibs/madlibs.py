# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    madlibs.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/01 14:39:19 by lamorim           #+#    #+#              #
#    Updated: 2021/08/01 14:52:05 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# String concatenation
# name = "Luís"
# printf("Hello " + name)
# printf("Hello {}".name)
# printf(f"Hello {name}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"\nComputer programming is so {adj}! It makes me so excited all the \
time becouse I love to {verb1}.\nStay hydrated and {verb2} like you are \
{famous_person}!"

print(madlib)
