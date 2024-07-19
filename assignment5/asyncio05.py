# example of waiting for the first task to complete
from random import random
import asyncio

# coroutine to execute in a new task
async def cooking(arg):
    # generate a random value between 0 and 1
    value = random() + 1
    print(f"Microwave ({arg}): Cooking {value}")
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'Microwave {arg} Finished cooking')
    return arg,value


# main coroutine
async def main():
    menus = ["Rice","Noodle","Curry"]
    # create many tasks
    tasks = [asyncio.create_task(cooking(i)) for i in menus]
    # wait for the first task to complete

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report result
    print(f'Completed task: {len(done)} task.')
    menu, time = done.pop().result()
    print(f' - {menu} is completed in {time}')
    print(f'Uncompleted task: {len(pending)} task.')

    # # get the first task to complete
    # first = done.pop()
    # print(first)


# start the asyncio program
asyncio.run(main())