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
    "quantity": "2",

}
# Posting a pixel
response = requests.post(url=pixel_posting_endpoint, json=pixel_posting_config, headers=headers)
print(response.text)