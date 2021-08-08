# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_start.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/07 18:19:47 by lamorim           #+#    #+#              #
#    Updated: 2021/08/07 18:40:01 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *

root = Tk()

# Creating a lable widget
myLable = Label(root, text="Hello World!")
# Shoving it onto screem
myLable.pack()
# loop for show window program
root.mainloop()
