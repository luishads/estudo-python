# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/04 22:41:51 by lamorim           #+#    #+#              #
#    Updated: 2021/08/04 23:22:37 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read();
    # print(content);

    soup = BeautifulSoup(content, 'lxml');
    ## print(soup.prettify());
    #courses_html_tags = soup.find_all('h5');
    ## print(courses_html_tags);
    course_card = soup.find_all('div', class_='card');
    for course in course_card:
        course_name = course.h5.text;
        course_prince = course.a.text;

        print(f'{course_name} costs {course_prince}');
