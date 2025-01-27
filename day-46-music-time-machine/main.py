from bs4 import BeautifulSoup
import requests



# Ask user to enter Date
# input_date = input("Which year do you want to travel to? Type the dat in this format: YYYY-MM-DD:")
input_date = "2011-09-17"

billboard_url = f"https://www.billboard.com/charts/hot-100/{input_date}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Make a call to Billboard.com to get the top 100 songs based upon entered date
response = requests.get(url=billboard_url, headers=header)
website_html = response.text

soup = BeautifulSoup(markup=website_html, features="html.parser")

# Find all h3 tags that are within an li tag and that have an id of "title-of-a-story"
song_tags = soup.select("li h3#title-of-a-story")

song_list = []

for tag in song_tags:
    # For each tag, get the text and strip of new lines/breaks
    song_list.append(tag.getText().strip())

print(f"song list: {song_list}")