import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "d6072ff3938016b92cb3f3b668cfa0e9"

weather_params = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())