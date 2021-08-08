# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_entry.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/07 18:19:47 by lamorim           #+#    #+#              #
#    Updated: 2021/08/07 19:48:51 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *

root = Tk()

myEntry = Entry(root, width=50, borderwidth=5, fg="#fff", bg="#000")
myEntry.pack()
myEntry.insert(0, "Enter Your Name here")
    # borderwidth chang width of the bord
    # We need put myEntry.pack() in another line otherwise the get() don't work

def myClick():
    hello = f'Hello {myEntry.get()}!'
    myLable = Label(root, text=hello)
    myLable.pack()

# Creating a lable widget
myButtons = Button(root, text="Print Name", padx=50, pady=30, command=myClick,\
fg="blue", bg="#fff").pack()

root.mainloop()
