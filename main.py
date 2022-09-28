import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")


MY_AGE = 21
MY_GENDER = "male"
MY_WEIGHT = 67
MY_HEIGHT = 173


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    # "x-remote-user-id":0,
}


exercise = input("Tell me what exercise you did: ")

post_data = {
    "query":exercise,
    "gender":MY_GENDER,
    "weight_kg":MY_WEIGHT,
    "height_cm":MY_HEIGHT,
    "age":MY_AGE,
}

exercise_reponses = requests.post(url=nutritionix_endpoint, json=post_data, headers=nutritionix_header)
exercise_data = exercise_reponses.json()
print(exercise_data)


sheety_api = os.getenv("SHEET_API")

upload_time = datetime.now()

headers = {"Authorization": "Bearer " + os.getenv("TOKEN")}

for exercise in exercise_data["exercises"]:
    post_data = {
        "workout":
        {
            "date":upload_time.strftime("%d/%m/%Y"),
            "time": upload_time.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url=sheety_api, json=post_data, headers=headers)
    print(sheet_response.text)







