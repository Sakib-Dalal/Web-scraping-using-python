from bs4 import BeautifulSoup
import requests

site_link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=site_link)

soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
movies_lst = [movie.get_text() for movie in movies]
movies_lst = movies_lst[::-1]

with open('./movies.txt', mode='w') as file:
    for movie in movies_lst:
        file.write(f'{movie}\n')

