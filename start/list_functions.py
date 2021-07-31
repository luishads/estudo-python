# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    list_functions.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 04:37:27 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 05:07:14 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

lucky_nbrs = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
friends.extend(lucky_nbrs)
print("\n" + str(friends))
friends.append("Creed")
print("\n" + str(friends))
friends.insert(2, "Pam")
print("\n" + str(friends))
friends.remove("Jim")
print("\n" + str(friends))
friends.clear()
print("\n" + str(friends))
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.pop()
print("\n" + str(friends))
print("\n" + str(friends.index("Kevin")))
print("\n" + str(friends.count("Jim")))
friends.sort()
print("\n" + str(friends))
lucky_nbrs.reverse()
print("\n" + str(lucky_nbrs))
friends2 = friends.copy()
print("\n" + str(friends2))
