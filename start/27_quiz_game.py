# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    27_quiz_game.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 23:53:02 by lamorim           #+#    #+#              #
#    Updated: 2021/08/01 00:14:36 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from questions_27 import Questions

questions_prompts = [
        "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
        "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
        "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
        ]

questions = [
        Questions(questions_prompts[0], "a"),
        Questions(questions_prompts[1], "c"),
        Questions(questions_prompts[2], "b")
        ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)
