import asyncio
import random

async def cook_rice():
    cooking_time = 1+random.random()
    print(f'Cooking rice... (will take {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('Rice is finish!')
    return 'rice ' , cooking_time

async def cook_noodle():
    cooking_time = 1+random.random()
    print(f'Cooking noodle... (will take {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('Noodle is finish!')
    return 'noodle ' , cooking_time

async def cook_curry():
    cooking_time = 1+random.random()
    print(f'Cooking curry... (will take {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('Curry is finish!')
    return 'curry ' , cooking_time

 
async def main():
    print('Cooking lunch...')
    
    # Create the tasks
    rice_task = asyncio.create_task(cook_rice())
    noodle_task = asyncio.create_task(cook_noodle())
    curry_task = asyncio.create_task(cook_curry())
    
    # Wait for the first dish to complete
    done, pending = await asyncio.wait(
        [rice_task, noodle_task, curry_task], 
        return_when=asyncio.FIRST_COMPLETED
    )
    
    for task in done:
        dish_name, cook_time = await task  # Await to get the result and cooking time
        print(f'Student A eats {dish_name} (cooking time: {cook_time:.10f} seconds)')
    
asyncio.run(main())