import json
import requests
from config import API_KEY

def get_json(url,**params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Bad Request'
    
def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    return 'Success write'

def get_data(data: json):
    for i in data['weather']:
        b=i['main']
    return f"Город: {data['name']}\n"\
        f"Погода: {b}\n"\
        f"Температура воздуха: {data['main']['temp']}\n"\
        f"Температура ощущается как: {data['main']['feels_like']}\n"\
        f"Давление: {data['main']['pressure']}\n"\
        f"Облачность: {data['clouds']['all']}%\n"\
        f"Скорость ветра:{data['wind']['speed']}"

city_name = input('Enter city name: ')
params = {'q': city_name, 'lang': 'ru', 'units': 'metric', 'appid': API_KEY}
url = 'https://api.openweathermap.org/data/2.5/weather'
data =  get_json(url=url, **params)
write_file(f'weather_{city_name.lower()}.json', data=data)
print(get_data(data=data))