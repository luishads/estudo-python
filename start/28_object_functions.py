# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    28_object_functions.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/01 00:18:10 by lamorim           #+#    #+#              #
#    Updated: 2021/08/01 00:31:42 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from student_26 import Student

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, False)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
