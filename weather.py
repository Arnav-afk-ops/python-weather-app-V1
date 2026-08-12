import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
city = input("Enter a City: ")

url = "https://api.openweathermap.org/data/2.5/weather"

request = {
    "appid": API_KEY,
    "q": city,
    "units": "metric"
}


def get_weather():
    response = requests.get(url, params=request)

    if response.status_code == 200:
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        print("=== WEATHER CLI ===")
        print(f"Temp : {temp}°C")
        print(f"Humidity : {humidity}%")
        print(f"Condition : {condition}")
        print(f"Description : {description}")

    else:
        print("Couldn't retrieve weather data :(")


get_weather()
