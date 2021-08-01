# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    student_26.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 23:28:03 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 23:35:42 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
