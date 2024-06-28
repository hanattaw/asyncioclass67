# example of running a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another coroutine
    await asyncio.sleep(1)

# create the coroutine
async def main():
    # execute my custom coroutine
    await custom_coro()
# check the type of the coroutine
asyncio.run(main())
