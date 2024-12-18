from os import getenv
from googletrans import Translator
import requests
import dotenv
import logging

dotenv.load_dotenv()
API_TOKEN = getenv('API_TOKEN')


logging.basicConfig(level=logging.INFO)


def get_random_quote():
    url = 'https://quotes88.p.rapidapi.com/random'
    headers = {
        'x-rapidapi-key': API_TOKEN,
        'x-rapidapi-host': 'quotes88.p.rapidapi.com'
    }
    translator = Translator()

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Выбрасывает исключение, если статус не 200
        raw_data = response.json()

        quote = raw_data.get('quote')  # Используем .get() для безопасного доступа
        author = raw_data['author'].get('name')
        born = raw_data['author'].get('born')
        died = raw_data['author'].get('died')
        if not quote or not author or not born:
            logging.error("Некорректные данные в ответе API")
            return "К сожалению, не удалось получить цитату. Попробуйте позже."
        if died != 'None':
            raw_quote = f'{quote}.\n{author}, {born}-{died}.'
        else:
            raw_quote = f'{quote}.\n{author}, {born}-по наст. время.'
        translated_quote = translator.translate(raw_quote, dest='ru')
        return translated_quote.text

    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка запроса: {e}")
        return "К сожалению, API сервиса временно недоступен. Попробуйте позже."

    except Exception as e:
        logging.error(f"Неизвестная ошибка: {e}")
        return "К сожалению, произошла ошибка. Попробуйте позже."


get_random_quote()
