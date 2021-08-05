# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lamorim <lamorim@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/04 23:26:24 by lamorim           #+#    #+#              #
#    Updated: 2021/08/05 19:49:27 by lamorim          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from bs4 import BeautifulSoup
import requests

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            #card_travel = job.find('li').string
            i_tag = job.i.decompose()
            card_travel = job.li.text
            if '0' in card_travel:
                #print(card_travel)
                company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_='srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                
                print(f'''
Company name: {company_name.strip()}
Required skills: {skills.strip()}
Experience: {card_travel}
More info: {more_info}
''')

find_jobs()
