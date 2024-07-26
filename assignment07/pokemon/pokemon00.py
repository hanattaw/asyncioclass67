import aiofiles
import asyncio
import json

# Correct the directory paths
pokemonapi_directory = 'c:/Users/Lenovo/OneDrive - Chitralada Technology Institute/Documents/Asy/asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'c:/Users/Lenovo/OneDrive - Chitralada Technology Institute/Documents/Asy/asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    # Read the content of the json file
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()
    print(contents)

asyncio.run(main())
