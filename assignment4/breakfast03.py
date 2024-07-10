# Concurrently breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare prepare ingruduebts")
    sleep(1)
    print("coffee. waiting...")
    await asyncio.sleep(5)  #2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():   #1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)  #2: pause, another task can be run
    print("eggs: ready")

async def main():   
    start = time()
    coffee_task = asyncio.create_task(make_coffee())    #schedule execution
    eggs_task = asyncio.create_task(fry_eggs())     #schedule execution
    # wait for completion, both tasks are scheduled for execution already
    await coffee_task,eggs_task#run task with await
    print(f"breakfast is ready in: {time() - start:.2f} min")


asyncio.run(main()) #run top-level function concurrently  