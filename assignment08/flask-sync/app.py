from flask import Flask, render_template
import requests as requests
import time
import random
from pypokemon.pokemon import Pokemon


app = Flask(__name__)

def get_pokemon(url):
    print(f"{time.ctime()} - get {url}")
    resp = requests.get(url)
    pokemon = resp.json()

    return pokemon

def get_pokemons():
    rand_list=[]
    for i in range(20):
        rand_list.append(random.randint(1,151))

    pokemon_data = []
    for number in rand_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)
        pokemon_object = Pokemon(pokemon_json)
        pokemon_data.append(pokemon_object)
    return pokemon_data

@app.route('/')
def index():
    start_time = time.perf_counter()
    pokemons = get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True, port=50000)