# check the type of a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #await another corouine
    await asyncio.sleep(1)

#create the coroutine
coro = custom_coro()
#check the type of the coroutine
print(type(coro))
