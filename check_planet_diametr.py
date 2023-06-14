import json # python check_planet_diametr.py runserver
import requests

url='https://swapi.dev/api/'
r = requests.get(url).json()

planet_api = r.get("planets")

def check_planet(url):
    names = []
    diameter = []

    for i in range(1,11):    
        response = requests.get(f'{url}{i}').json()
        if response.get('detail') == 'Not found':
            continue
        if response.get('diameter') == 'n/a':
            continue
        max_diameter = response.get('diameter')
        namer = response.get('name')
        names.append(namer)
        diameter.append(int(max_diameter))
        max_index = diameter.index(max(diameter))

    print(names[max_index],':',max_diameter)

check_planet(planet_api)

