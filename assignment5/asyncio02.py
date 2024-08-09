# example of waiting for the first task to complete
from random import random
import asyncio


async def task_coro(arg):
    # Simulate asynchronous work by sleeping for a random amount of time
    value = random()
    await asyncio.sleep(value)
    # Report the value of the task
    print(f'>task ({arg}) done with {value}')

async def main():
    # Create 10 tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # Wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # Print a message when the first task completes
    print('Done')
    # Get the first completed task
    first = done.pop()
    # Print the first completed task
    print(first)

# Start the asyncio program

asyncio.run(main())

