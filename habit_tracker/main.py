import datetime
import requests

USERNAME = "vivekking"
TOKEN = "kjhhdfdsfkjhsdhfkjkhsdff"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

# TODO:- creating a user on pixela.

user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# with requests.post(url=pixela_endpoint, json=user_parameter) as response:
#     print(response.text)

# TODO:- creating a graph on pixela.

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "color": "ajisai",
    "type": "float",

}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.datetime.now()

# TODO:- posting a pixel to the graph.

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today ? "),

}


response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", json=pixel_data, headers=headers)
print(response.text)

# TODO:- updating a existing pixel with new data.

pixel_update = {
    "quantity": "3"
}

# response = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/20220426", json=pixel_update, headers=headers)
# print(response.text)

# TODO:- Deleting a pixel.

# response = requests.delete(url=f"{graph_endpoint}/{GRAPH_ID}/20220426", headers=headers)
# print(response.text)
