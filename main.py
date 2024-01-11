import requests
import datetime as dt
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#### Create user #####
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

#### Create graph #####
GRAPH_ID = "graph1"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Exercise Graph",
    "unit": "mins",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

#### Post pixel #####
post_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
date = dt.datetime.now()

post_pixel_params = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you exercise today?"),
}
response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
response.raise_for_status()
print(response.text)

#### Update pixel #####
update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime("%Y%m%d")}"
update_pixel_params = {
    "quantity": "35",
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
response.raise_for_status()
print(response.text)

#### Delete pixel #####
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime("%Y%m%d")}"
response = requests.delete(url=delete_endpoint, headers=headers)
response.raise_for_status()
print(response.text)