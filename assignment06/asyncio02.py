# example of an asynchronous interator with async for loop
import asyncio

class AsyncIterator:
    def __init__(self):
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):

        if self.counter >= 10:
            raise StopAsyncIteration

        self.counter += 1

        await asyncio.sleep(1)

        return self.counter

async def main():

    async for item in AsyncIterator():
        print(item)

asyncio.run(main())