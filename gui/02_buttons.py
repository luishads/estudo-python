# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_buttons.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/07 18:19:47 by lamorim           #+#    #+#              #
#    Updated: 2021/08/07 19:17:52 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *

root = Tk()

def myClick():
    myLable = Label(root, text='Look! I clicked the button!!').pack()

# Creating a lable widget
myButtons = Button(root, text="Click me", padx=50, pady=30, command=myClick,\
fg="blue", bg="#fff").pack()
    # padx and pady change size button.
    # command=myClick make action on click
    # fg change text color and bg change background color

root.mainloop()
