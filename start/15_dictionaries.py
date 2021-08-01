# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    15_dictionaries.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/31 15:30:33 by lamorim           #+#    #+#              #
#    Updated: 2021/07/31 15:45:35 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

month_conversions = {
        1: "January",
        2: "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
        }

print(month_conversions["Nov"])
print(month_conversions.get("Dec"))
print(month_conversions.get("Luv", "Not a valid key"))
print(month_conversions[2])
