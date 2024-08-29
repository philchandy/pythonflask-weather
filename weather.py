from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

API_key = os.getenv('API_KEY')

def get_current_weather(zip_code = "10001"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={API_key}'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    print('\n***GET WEATHER***\n')

    zipcode = input("\nPlease input a zipcode:")

    weather_data = get_current_weather(zipcode)
    
    print('\n')
    pprint(weather_data)