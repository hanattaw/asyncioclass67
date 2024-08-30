# example of using an asyncio queue without blocking
from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    start_time = time.time()
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    end_time = time.time()  # Record the end time
    print(f'Producer: Done. Total time: {end_time - start_time:.2f} seconds')
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    start_time = time.time()
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
    end_time = time.time()
    print(f'Consumer: Done. Total time: {end_time - start_time:.2f} seconds')
# entry point coroutine
async def main():
    start_time = time.time()

    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.time()
    print(" ")
    print(f'All: Done. Total time: {end_time - start_time:.2f} seconds')

 
# start the asyncio program
asyncio.run(main())