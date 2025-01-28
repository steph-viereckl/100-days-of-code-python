from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Ask user to enter Date
input_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD:")

# Get year so it can be used later on when searching tracks and naming the playlist
year = input_date[0:4]
# input_date = "2011-09-17" # For testing
billboard_url = f"https://www.billboard.com/charts/hot-100/{input_date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Make a call to Billboard.com to get the top 100 songs based upon entered date
response = requests.get(url=billboard_url, headers=header)
website_html = response.text

# Use scraper to get the html of the webpage
soup = BeautifulSoup(markup=website_html, features="html.parser")
# Find all h3 tags that are inside an li tag and that have an id of "title-of-a-story"
song_tags = soup.select("li h3#title-of-a-story")

song_list = []

for tag in song_tags:
    # For each tag, get the text and strip of new lines/breaks
    song_list.append(tag.getText().strip())

load_dotenv()
client_id = os.environ.get("CLIENT_ID", "Spotify Client Id cannot be found")
client_secret = os.environ.get("CLIENT_SECRET", "Spotify Client Secret cannot be found")

oauth_response = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://example.com",
    scope="playlist-modify-private"
)

sp = spotipy.Spotify(auth_manager=oauth_response)

user_id = sp.current_user()["id"]

song_uris = []

# Use the following to create a list of 10 when testing
# for num in range(0,20):
#     song = song_list[num]
for song in song_list:

    result = sp.search(q=f"track:{song} year:{year}", type="track", limit="50")
    # pprint.pp(result)
    try:

        # Using the returned songs, get the most popular (this is to try and avoid kidzbop being chosen)
        most_popular_track = None
        most_popular_track_popularity = 0

        for track in result["tracks"]["items"]:
            print(f"for {track["name"]} by {track["artists"][0]["name"]} has popularity of {track["popularity"]}")
            if int(track["popularity"]) > most_popular_track_popularity:
                most_popular_track = track
                most_popular_track_popularity = int(track["popularity"])

        # song_uris.append(result["tracks"]["items"][0]["uri"])
        song_uris.append(most_popular_track["uri"])

    except:
        print("Song doesn't exist")

print(song_uris)

# Create a new Playlist based upon the user's inputted year
playlist = sp.user_playlist_create(user=user_id, public=False, name=f"Top 100 Songs in {year}", collaborative=False)
# pprint.pp(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

