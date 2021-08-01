# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    functions.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 13:56:04 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 14:10:51 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def say_hi(name):
    print("Hello User " + name)
def name_age(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike")
say_hi("Jim")
name_age("Keven", 40)
