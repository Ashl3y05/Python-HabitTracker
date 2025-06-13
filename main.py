import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "7a6sf5sdfs6df76dys78",
    "username": "ashley",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)