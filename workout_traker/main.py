import requests
from datetime import datetime

GENDER = "male"
AGE = 22
HEIGHT = 164
WEIGHT = 50

APP_ID = "264e1069"
API_KEY = "222b18b472747408210f39e42246a8d8"

google_sheet_endpoint = "https://api.sheety.co/ba0808a8b06846e12417119a5cae5d46/workoutTracking/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%H:%M:%S")

exercise_text = input("Tell me which exercises did you today? ")

parameter = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE,

}

nutritionix_response = requests.post(url=exercise_endpoint, json=parameter, headers=nutritionix_headers)
data = nutritionix_response.json()['exercises']

sheet_input = {}

for item in data:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories']
        }
    }
    headers ={"Authorization": "Bearer kjjshdfksfkjshdfishdfkkjh"}
    response = requests.post(url=google_sheet_endpoint, json=sheet_input, headers=headers)
    print(response.text)


