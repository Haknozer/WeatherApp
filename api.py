import redis
from dotenv import load_dotenv
import requests
import os
import json



def fetchAndStore(redis_key_location):
    expiration = 42000
    load_dotenv("key.env")
    api_key = os.getenv("API_KEY")

    redis_client = redis.StrictRedis(host="localhost",port=6379,decode_responses=True)

    cached_data = redis_client.get(redis_key_location)

    if cached_data:
        print("Pulling data from redis")
        return json.loads(cached_data)
    else:
        print("Pulling data from api")
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{redis_key_location}?key={api_key}"
        requestWeather = requests.get(url)
        if requestWeather.status_code == 200: 
            responseJson = requestWeather.json()
            redis_client.set(redis_key_location,json.dumps(responseJson),ex=expiration)
            return responseJson
