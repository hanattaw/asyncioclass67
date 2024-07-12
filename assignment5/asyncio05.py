from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = 1 + random()
    # block for a moment
    print(f'Microwave ({arg}): Cooking {value} seconds...')
    await asyncio.sleep(value)
    print(f'Microwave ({arg}) finished cooking')
    return arg, value
    

# main coroutine
async def main():
    menu = ["Rice", "Noodle", "Curry"]
    tasks = [asyncio.create_task(task_coro(i)) for i in menu]
  
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f'complete task: {len(done)} ')
    first = done.pop()
    print(f'{first.result()[0]} is completed in {first.result()[1]}')
    print(f'uncomplete task: {len(pending)}')
    

# start the asyncio program
asyncio.run(main())
