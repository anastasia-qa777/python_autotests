import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '995257f12654fd76bcdf1eb35487ae6c'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
TRAINER_ID='9034'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons',params={'trainer_id':TRAINER_ID})
    assert response.status_code==200


@pytest.mark.parametrize('key, value',[('name','Капибара'),('trainer_id', TRAINER_ID),('id', '124164')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
    assert response_parametrize.json()["data"][0][key] == value