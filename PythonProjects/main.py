import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '995257f12654fd76bcdf1eb35487ae6c'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}

body_registration = {
"trainer_token": TOKEN,
"email": "почта",
"password": "пароль"}
  
body_confirmation ={
"trainer_token": TOKEN
}

body_create = {
    "name": "Капибара",
    "photo_id": 69
}

body_change={
    "pokemon_id": "124163",
    "name": "Капи Капи",
    "photo_id": 2
}

body_in_pokeball={
    "pokemon_id": "124163"
}

body_knockout={
    "pokemon_id": "124163"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration) 
 print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation) 
print(response_confirmation.text)'''

response_create=requests.post(url = f'{URL}/pokemons', headers=HEADER,json=body_create)
print(response_create.text) 
'''pokemon_id = response_create.json()["id"]
'''
response_change=requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_change )
print(response_change.text)  

response_in_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_in_pokeball)
print(response_in_pokeball.text)
'''
response_knockout=requests.post(url=f'{URL}/pokemons/knockout',headers=HEADER,json=body_knockout)
print(response_knockout.json)
print(response_knockout.text)'''