from os import getenv
import requests
import dotenv
import json

dotenv.load_dotenv()
API_TOKEN = getenv('API_TOKEN')


def get_random_quote():
    url = 'https://quotes88.p.rapidapi.com/random'
    headers = {'x-rapidapi-key': API_TOKEN,
               'x-rapidapi-host': 'quotes88.p.rapidapi.com'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        raw_data = response.json()
        # print(json.dumps(raw_data, indent=4, ensure_ascii=False))
        quote = raw_data['quote']
        author = raw_data['author']['name']
        born = raw_data['author']['born']
        died = raw_data['author']['died']
        return (f'{quote}.\n'
                f'{author}, {born}-{died}')
    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)
        return "К сожалению, API сервиса временно недоступен. Попробуйте позже."


get_random_quote()

