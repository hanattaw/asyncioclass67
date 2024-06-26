# example of running a coroutine
import asyncio
#define a coroutine
async def custon_coro():
    # awit another corotine
    await asyncio.sleep(1)

#Main corotine
async def main():
    # execute my custom corotine
    await custon_coro()

# start the corotine program
asyncio.run(main())