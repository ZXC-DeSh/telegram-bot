import json
import requests
fast_ship = ""
url='https://swapi.dev/api/'
r = requests.get(url).json()

starships_api = r.get('starships')

def check_starships(url):

  names = []
  spedyy = []

  for i in range(1, 11):
    response = requests.get(f'{url}/{i}').json()
    if response.get('detail') == 'Not found':
      continue
    if response.get('max_atmosphering_speed') == 'n/a':
      continue

    max_speed = response.get('max_atmosphering_speed')
    namer = response.get('name')
    names.append(namer)
    spedyy.append(int(max_speed))
    max_index = spedyy.index(max(spedyy))

  print(names[max_index])

check_starships(starships_api)