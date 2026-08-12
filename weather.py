import requests
import json
API_KEY = "ENTER YOUR API HERE"
city = input("Enter a City : ")


url = "https://api.openweathermap.org/data/2.5/weather"
request = {
    "appid" : API_KEY,
    "q": city,
    "units":"metric"

}


def get_request() :
 response = requests.get(url,params = request)
 data = response.json()
 temp = data["main"]["temp"]
 humidity = data["main"]["humidity"]
 condition = data["weather"][0]["main"]
 description = data["weather"][0]["description"]

 print("===  WEATHER CLI  ===")
 print(f"Temp : {temp}°C")
 print(f"Humidity : {humidity}%")
 print(f"Condition : {condition}")
 print(f"Description : {description}")


if response.status_code == 200 :
 get_request()



else :
 print("Couldn't retrieve weather data :(")