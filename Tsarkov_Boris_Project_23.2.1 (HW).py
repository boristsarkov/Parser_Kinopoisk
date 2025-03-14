import requests
from bs4 import BeautifulSoup

user_login = '2576697'
url = f'https://www.kinopoisk.ru/user/{user_login}/votes/'

r = requests.get(url)

with open('Kinopoisk', 'w', encoding='utf-8') as output_file:
   output_file.write(r.text)


soup = BeautifulSoup(r.text, 'lxml')
entries = soup.find_all('div', class_='item')

print(len(entries))
"""data = []
for entry in entries:
   td_film_details = entry.find('div', class_='info')
   film_name = td_film_details.find('a').text
   data.append({'film_name': film_name})

print(data)"""
