# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    23_reading_files.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 20:13:57 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 20:33:20 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

employee_file = open("file_for_23.txt", "r")

#if employee_file.readable:
#    print(employee_file.read())

#print(employee_file.readline())
#print(employee_file.readline())

#print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
