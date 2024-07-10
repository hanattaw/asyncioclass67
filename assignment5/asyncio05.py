import asyncio
from random import random

async def cook_dish(dish_name):
    cook_time = 1 + random()  # Random cooking time between 1 to 2 seconds
    await asyncio.sleep(cook_time)
    return f'{dish_name} Cooking {cook_time:.2f} seconds...'

async def main():
    # Create tasks for cooking each dish concurrently
    rice_task = asyncio.create_task(cook_dish('Microwave (Rice):'),name='rice')
    noodle_task = asyncio.create_task(cook_dish('Microwave (Noodle):'),name='noodle')
    curry_task = asyncio.create_task(cook_dish('Microwave (Curry):'),name='Curry')

    # Wait until the first task completes
    done, pending = await asyncio.wait(
        [rice_task, noodle_task, curry_task],
        return_when=asyncio.FIRST_COMPLETED
    )


    results = await asyncio.gather(rice_task, noodle_task, curry_task)
    # Print all results
    for result in results:
        print(result)

    # Retrieve and print the result of the first completed task
    first_completed_task = done.pop()
    
    print(f'{first_completed_task.get_name()} Finished cooking')
    print(f'Completed task1: \n -{first_completed_task.result()}')

# Run the main coroutine
asyncio.run(main())
