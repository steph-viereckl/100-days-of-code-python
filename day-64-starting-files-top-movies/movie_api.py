from pprint import pprint

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

class MovieFinder:

    def __init__(self, title_to_search):

        load_dotenv()
        # Version 3 is controlled by one of either a single query parameter, api_key, or by using your access token as a Bearer token. You can request an API key by logging in to your account on TMDB and clicking here.
        # self.api_key = os.environ["MOVIES_API_KEY"]
        api_token = os.environ["MOVIES_TOKEN"]

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_token}"
        }

        params = {
            "query": title_to_search
        }

        response = requests.get(url=url, params=params, headers=headers)
        self.search_results = response.json()["results"]
        # pprint(f"Search results: {self.search_results['results']}")
        # pprint(f"Search results: {self.search_results['total_results']}")



# movieFinder = MovieFinder("Lord of the Rings")