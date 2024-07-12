from random import random
import asyncio


async def task_coro(arg):
    value = 1 + random()
    print(f'Microwave {arg}: {value} seconds')
    await asyncio.sleep(value)
    print(f'Microwave {arg}: finish cooking')
    return arg, value  # Return both argument and the time taken

async def main():
    menu = ["Rice", "Noodles", "Curry"]
    tasks = [asyncio.create_task(task_coro(i)) for i in menu]
    
    # Wait for all tasks to complete with a timeout
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # Find the task that completed first
      
    
    print(f'Complete task: {len(done)} task')
    first = done.pop()   
    arg, value = first.result()  # Get the result of the completed task
    print(f'- {arg} completed in {value} seconds')    
    print(f'Uncomplete task: {len(pending)} tasks ')

asyncio.run(main())
