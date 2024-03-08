import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 60.1
HEIGHT_CM = 167.8
AGE = 23

APP_ID = "50b55cd2"
APP_KEY = "10deb78f1d2d2ef0709b27c188646b9a"

exercise_text = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
print(response.json())

all_exercises = response.json()["exercises"]

sheety_endpoint = "https://api.sheety.co/924cf6f00c1cf084c1e529961a3e0c59/workoutTracking/workouts"

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
sheety_headers = {"Authorization": "Bearer aiwuehfajsdnkfadifh"}

for exercise in all_exercises:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(sheety_response)
