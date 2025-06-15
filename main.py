import requests
from datetime import datetime

USERNAME = "ashl3y"
TOKEN = "7a6sf5sdfs6df76dys78"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# Creating a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# Creating a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

formatted_date_today = today.strftime("%Y%m%d")

pixel_posting_config = {
    "date": formatted_date_today,
    "quantity": "20",

}
# Posting a pixel
# response = requests.post(url=pixel_posting_endpoint, json=pixel_posting_config, headers=headers)
# print(response.text)

yesterday = datetime(month=6, day=14, year=2025)
formatted_date_yesterday = yesterday.strftime("%Y%m%d")
pixel_updating_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date_yesterday}"

pixel_posting_update = {
    "date": formatted_date_yesterday,
    "quantity": "10",

}
# Updating a pixel
response = requests.put(url=pixel_updating_endpoint,json=pixel_posting_update,headers=headers)
print(response.text)