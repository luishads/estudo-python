# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    18_for_loop.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 16:11:59 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 16:27:56 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

for letter in "42 School":
    print(letter)

print("")
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

print("")
for index in range(10):
    print(index)

print("")
for index in range(3, 10):
    print(index)

print("")
for index in range(len(friends)):
    print(friends[index])

print("")
for index in range(5):
    if index == 0:
        print("first interation")
    else:
        print("Not first")
