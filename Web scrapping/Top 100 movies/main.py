import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

movies_name = soup.findAll(name="h3", class_="title")

movies = []
for name in movies_name:
    movies.append(name.get_text())

movies.reverse()

with open("movies.txt", mode='w') as file:
    for name in movies:
        file.write(f"{name}\n")



