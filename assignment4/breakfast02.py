# Concurrently breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare prepare ingruduebts")
    sleep(1)
    print("coffee. waiting...")
    await asyncio.sleep(5)  #2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():   
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)  #2: pause, another task can be run
    print("eggs: ready")

async def main():   
    start = time()
    await make_coffee(),fry_eggs() #run task with await
    print(f"breakfast is ready in: {time() - start:.2f} min")


asyncio.run(main()) #run top-level function concurrently  