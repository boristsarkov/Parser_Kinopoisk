import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_online_content(type_content, page_num):
    data = []
    url = f'https://www.kinoafisha.info/online/{type_content}/?page={page_num}'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    entries = soup.find_all('div', class_='movieList_item movieItem movieItem-grid grid_cell3')
    for entry in entries:
        div_film_details = entry.find('div', class_='movieItem_info')
        film_name = div_film_details.find('a').text
        mark = div_film_details.find('span', class_='mark_num').text
        genre = div_film_details.find('span', class_='movieItem_genres').text
        year_country = div_film_details.find('span', class_='movieItem_year').text
        year = year_country.split(' ')
        data.append({'film_name': film_name, 'mark': mark, 'genre': genre, 'year': year[0].replace(',', ''), 'country': year[1]})

    return data

online_content = get_online_content('movies', 15)
df = pd.DataFrame(online_content)
df.to_excel('online_content.xlsx')

