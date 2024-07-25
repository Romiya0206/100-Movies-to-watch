import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
movie_response = requests.get(URL)
movie_text= movie_response.text

movie_titles = []

soup = BeautifulSoup(movie_text, "html.parser")
title = soup.find_all(name="h3", class_="title")
for n in title:
    tit = n.getText()
    movie_titles.append(tit)

movie_names = [x for x in movie_titles[::-1]]

with open("movie.txt", "w") as file:
    file.writelines([str(i)+'\n' for i in movie_names])

print(len(movie_titles))
