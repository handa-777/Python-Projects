import requests
from datetime import datetime

USERNAME = "han"
TOKEN = "safdqwerjiko"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

value_endpoint = f"{graph_endpoint}/{GRAPH}"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

value_config = {
    "date": formatted_today,
    "quantity": "6.0"
}

# response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(response.text)

update_endpoint = f"{value_endpoint}/{formatted_today}"

update_config = {
    "quantity": "12.0"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
