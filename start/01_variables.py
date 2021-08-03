# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_variables.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 04:11:25 by lamorim           #+#    #+#              #
#    Updated: 2021/08/02 22:22:34 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

character_name = "John" # A variable can receive some type of data
character_age = "35" # In this exemples we are using string

# We can use our variables to call their values and use in our functions
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " yers old.")

# We can reassinned variables values
character_name = "Mike"
print("He really like the name " + character_name + ",")
print("but don't like being " + character_age + ".")
