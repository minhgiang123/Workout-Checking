import requests

APP_ID = "61f13d61"
API_KEY = "c23b22b28c8acb6bf4ce7f61e9ca80e1"

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

reponses = requests.post(url=nutritionix_endpoint, json=post_data, headers=nutritionix_header)
exercise_data = reponses.json()
print(exercise_data)



