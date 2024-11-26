from dotenv import load_dotenv
import requests
import methods 
import api
import os

load_dotenv("key.env")
api_key = os.getenv("API_KEY")

while True:
    location = input("Enter The Location (Example: London): ")
    responseJson = api.fetchAndStore(location)

    if responseJson:
        break
    else:
        print("Wron location again enter")



while True:
    print("Daily weather : 1")
    print("weekly weather : 2")
    print("Exit: 3")
    choose = input("Your choice: ")
    if choose == "1":
        for weather in responseJson["days"]:
            methods.dailyWeather(weather)
            methods.hoursWeather(weather)
            break
    elif choose == "2":
        for x in range(7):
            path = responseJson["days"][x]
            methods.weeklyWeather(path)
        print("WEEKLY WEATHER")
        methods.tabulatePrint()
    elif choose == "3":
        break
    else:
        print("Wrong choose")

