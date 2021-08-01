# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    24_writing_to_files.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 20:35:25 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 21:04:38 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Appending to a file
employee_file = open("file_for_24.txt", "a")

employee_file.write("\nToby - Human Resources")

employee_file.close()

# Create a file or subscribe a existent file
employee_file = open("file_for_24_1.txt", "w")

employee_file.write("\nToby - Human Resources")

employee_file.close()
