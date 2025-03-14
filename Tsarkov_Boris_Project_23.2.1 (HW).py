import requests
from bs4 import BeautifulSoup

user_login = 2576697
page_num = 1
url = f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/{page_num}/#list'
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

entries = soup.find_all('div', class_='item')

print(len(entries))
