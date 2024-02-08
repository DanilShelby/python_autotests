"""
requeststest test api
"""
import requests
URL='https://api.pokemonbattle.me/v2'
HEADER={'Content-Type': 'application/json', 'trainer_token': '688bdb324c148e72bdce3f1aa2a8ee8d'}

def test_get_trainers():
    """
    KTI-1. Get trainers by trainer id
    """
    response=requests.get(url=f'{URL}/trainers', params= {'trainer id': 4994})
    assert response.status_code == 200, 'Unexpected status code'
    print(f'статус код:{response.status_code}. Сообщение: {response.text}')
