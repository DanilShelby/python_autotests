"""
requeststest test api
"""
import requests
URL='https://api.pokemonbattle.me/v2'
HEADER={'Content-Type': 'application/json', 'trainer_token': '688bdb324c148e72bdce3f1aa2a8ee8d'}
body={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
response=requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'статус код:{response.status_code}. Сообщение: {response.text}')
"""
requeststest test api
"""
import requests
URL='https://api.pokemonbattle.me/v2'
HEADER={'Content-Type': 'application/json', 'trainer_token': '688bdb324c148e72bdce3f1aa2a8ee8d'}
body={
    "pokemon_id": "29927",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response=requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'статус код:{response.status_code}. Сообщение: {response.text}')
"""
requeststest test api
"""
import requests
URL='https://api.pokemonbattle.me/v2'
HEADER={'Content-Type': 'application/json', 'trainer_token': '688bdb324c148e72bdce3f1aa2a8ee8d'}
body={
    "pokemon_id": "29927"
}
response=requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'статус код:{response.status_code}. Сообщение: {response.text}')