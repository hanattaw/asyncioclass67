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
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    #open a file for write the list of moves into
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))


asyncio.run(main())