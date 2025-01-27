import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
# Use Beautiful Soup to parse the website url
soup = BeautifulSoup(markup=response.text, features="html.parser")
# Get all the movie title tags
movie_title_tags = soup.find_all(name="h3", class_="title")
# For each tag, extract the text (i.e. "1) The Godfather")
movie_titles = [tag.getText() for tag in movie_title_tags]
# movie_titles_reversed = movie_titles[::-1]
# print(f"movie_titles_reversed: {movie_titles_reversed}")

movies_to_watch_file = ""

for title in reversed(movie_titles):
    movies_to_watch_file += f"{title}\n"

with open("movies-to-watch.txt", "w") as file:
    file.write(movies_to_watch_file)














