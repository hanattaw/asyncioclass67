import aiofiles
import asyncio
import json

pokermonapi_directory = './assignment07/pokemon/pokemonapi'
pokermonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    # Read the contents of the json file.
    async with aiofiles.open(f'{pokermonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()

    # load it into a dictionary and create a list of moves
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    # open a new file to write the list of moves into.
    async with aiofiles.open(f'{pokermonmove_directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))

asyncio.run(main())