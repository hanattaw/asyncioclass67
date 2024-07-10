#Cook Wait
import asyncio
import random
#all def
async def cook_rice():
    cooking_time = 1 + random.random()
    print(f'Cooking Rice... ({cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('Rice is Finished!')
    return 'rice ' , cooking_time

async def cook_noodle():
    cooking_time = 1 + random.random()
    print(f'Cooking Noodle... ({cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('Noodle is Finished!')
    return 'noodle ' , cooking_time

async def cook_curry():
    cooking_time = 1 + random.random()
    print(f'Cooking Curry... ( {cooking_time:.10f} seconds)')
    await asyncio.sleep(cooking_time)
    print('Curry is Finished!')
    return 'curry ' , cooking_time

 
async def main():
    print('Cooking Food...')
    
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
        dish_name, cook_time = await task 
        print(f'Student A Eatting {dish_name} (cooking time: {cook_time:.10f} seconds)')
    
asyncio.run(main())