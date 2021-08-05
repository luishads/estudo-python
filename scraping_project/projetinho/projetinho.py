
from bs4 import BeautifulSoup
import requests

link = input("Coloque o link: ")

html_text = requests.get(link).text

soup = BeautifulSoup(html_text, 'lxml');
paragraths = soup.find_all('p')
for paragrath in paragraths:
    content = paragrath.text

    print(f'{content}');
