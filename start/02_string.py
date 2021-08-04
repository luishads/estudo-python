# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_string.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 04:11:11 by lamorim           #+#    #+#              #
#    Updated: 2021/08/04 00:02:06 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# We can use string with doble and single quots
print("New\nline")
print('This \"work\" good')

print()
# We can use triple quots for multi-line string
print('''This text has more than
one line, and it\'s works!''')

print()
# String concatenation and the Format method
name = "lamorim"
age = 25
# We can concatenation string like this:
print('My name is ' + name + ' and I am ' + str(25))
# The better way to do concatenation string is the format method
print('My name is {0} and I am {1}'.format(name, age))
#In Python 3.6+ we can make
print('My name is {name} and I am {age}')
# We can format outputs with fromat method
print('{0:.3f}'.format(1.0 / 3))
# We can cancel the new line deful print
print('Not a', end=' ')
print('new ', end='')
print('line.')

# TODO Escape sequences

phrase = "Look the Power"
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper()) # = True
print(len(phrase)) # = 14
print(phrase[0]) # = L
print(phrase.index("L")) # = 0
print(phrase.replace("Look", "See"))
