from os import getenv
import requests

API_TOKEN = getenv('API_TOKEN')


def get_movie_data():
    url = 'https://moviedatabase8.p.rapidapi.com/Search/Incep'
    headers = {'x-rapidapi-key': API_TOKEN}
    response = requests.get(url, headers=headers)
    if response:
        return response.json()
    else:
        print('Что-то пошло не так с url или headers')


def get_movie_by_name(title):
    url = f'https://moviedatabase8.p.rapidapi.com/FindByTitle/{title}'
    headers = {'x-rapidapi-key': API_TOKEN}
    response = requests.get(url, headers=headers)
    if response:
        data = (f'Название - {response['title']}\n'
                f'Слоган - {response['tagline']}\n'
                f'Жанр - {response['genres']}\n'
                f'Описание - {response['overview']}\n'
                f'Страна производства - {response['production_countries']}\n'
                f'IMDb - {response['popularity']}\n'
                )
        return data
    else:
        print('Запрошеный фильм не найден в базе.')
