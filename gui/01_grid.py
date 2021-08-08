# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_grid.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/07 18:19:47 by lamorim           #+#    #+#              #
#    Updated: 2021/08/07 18:51:52 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *

root = Tk()

# Creating a lable widget
myLable1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLable2 = Label(root, text="My name is Luís")
# Shoving it onto screem
# myLable1.grid(row=0, column=0)
myLable2.grid(row=1, column=1)
# loop for show window program
root.mainloop()
