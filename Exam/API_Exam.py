import requests
import json
from pprint import pprint
import pandas as pd

people_url = "http://swapi.dev/api/people/"
films_url = "http://swapi.dev/api/films/"

people_response = requests.get(people_url).json()['results']
films_response = requests.get(films_url).json()['results']

people_json_results = json.dumps(people_response, sort_keys=True, indent=4)
films_json_results = json.dumps(films_response, sort_keys=True, indent=4)

people_json_results = json.dumps(people_response, sort_keys=True, indent=4)
films_json_results = json.dumps(films_response, sort_keys=True, indent=4)
with open('./people.csv', 'w+') as f:
    f.write(people_json_results)
with open('./films.csv', 'w+') as f:
    f.write(films_json_results)