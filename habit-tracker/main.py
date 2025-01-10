import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "stepythonie"
TOKEN = "abcdefghijk"

# user_parameters = {
#     "token":,
#     "username":,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(f"Response: {response.text}")

# graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
#
# graph_parameters = {
#     "id": "squatgraph1",
#     "name": "Back Squat Graph",
#     "unit": "Lbs",
#     "type": "int",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(graph_response.text)

GRAPH_ID = "squatgraph1"

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
specific_date = datetime(year=2025, month=1, day=1)
print(formatted_date)
pixel_parameters = {
    "date": formatted_date,
    "quantity": "85"
}

pixel_headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=pixel_headers)
# print(graph_response.text)


graph_date = datetime(year=2025, month=1, day=9).strftime("%Y%m%d")

update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{graph_date}"
print(update_pixel_endpoint)

pixel_parameters = {
    "quantity": "100"
}

pixel_headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.put(url=update_pixel_endpoint, json=pixel_parameters, headers=pixel_headers)
# print(graph_response.text)


graph_response = requests.delete(url=update_pixel_endpoint, headers=pixel_headers)
print(graph_response.text)