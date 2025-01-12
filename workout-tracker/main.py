import requests
from datetime import datetime
import os

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_json = {
    "query": input("What activity did you do? ")
}

nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
nutritionix_response = requests.post(url=nutritionix_endpoint, json=nutritionix_json, headers=nutritionix_header)
nutritionix_response.raise_for_status()
exercise_data = nutritionix_response.json()
print(exercise_data)

today = datetime.now()
day = today.strftime('%Y/%m/%d')

for exercise in exercise_data["exercises"]:

    sheety_json = {
            "workout": {
                "date": today.strftime('%Y/%m/%d'),
                "time": today.strftime('%H:%M'),
                "exercise": exercise["name"],
                "duration": str(exercise["duration_min"]),
                "calories": str(exercise["nf_calories"])
            }
    }

    # {'workout': {'date': '2025/01/12', 'time': datetime.time(10, 51, 21, 12287), 'exercise': 'ski', 'duration': '61.26', 'calories': '643.23'}}
    print(sheety_json)

    # You can add a message if the environment variable is not found
    SHEETY_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN", "Sheety Bearer Token does not exist")
    SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Sheety Endpoint was not found")
    header = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_json, headers=header)
    sheety_response.raise_for_status()

