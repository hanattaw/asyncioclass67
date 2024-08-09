import aiofiles
import asyncio
import json

pokermonapi_directory = './assignment07/pokemon/pokemonapi'
pokermonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    # read the contents of the json file.
    async with aiofiles.open(f'{pokermonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()
    
    # load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    print(pokemon['name'])

asyncio.run(main())