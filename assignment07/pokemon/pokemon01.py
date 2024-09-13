import aiofiles
import asyncio
import json

pokemonapi_directory = 'c:/Users/Lenovo/OneDrive - Chitralada Technology Institute/Documents/Asy/asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'c:/Users/Lenovo/OneDrive - Chitralada Technology Institute/Documents/Asy/asyncioclass67/assignment07/pokemon/pokemonmove'

async  def main():
    #read the content of the json file
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()

    #load it into a dictionary and create a list of moves
    pokemon = json.loads(contents)
    print(pokemon['name'])


asyncio.run(main())