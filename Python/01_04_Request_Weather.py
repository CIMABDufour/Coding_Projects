# Beginner Project
# Get Weather from places
#  Build a simple program that fetches and displays the current weather for a given city using a weather API.

import requests

lat = 46.813877
long = -71.207977
api_key = '8c4f1eb8962fa1c5fd011099337782db' #this api key isn't available.
city = input('Location name ? : ')

# url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

get_info = requests.get(url).json()

Location_name = get_info['name']
celsius_info = get_info['main']['temp'] - 273.15

print(f'The weather in {Location_name} is : {round(celsius_info)} °C')
