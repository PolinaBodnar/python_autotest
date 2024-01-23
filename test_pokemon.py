import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type' : 'application/json', 'treiner_token' : 'd4b14fab7a08c2787fd21d56d777e2d1'}

body = {
    "name": "Pomodoro",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(response)

def test_put_pokemons():
    response = requests.put(url=f'{URL}/pokemons', headers=HEADER)
print(response)

def test_post_trainers_add_pokeball():
    response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(response)


def test_get_trainers():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id ': 3707}, json=body, headers=HEADER, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'