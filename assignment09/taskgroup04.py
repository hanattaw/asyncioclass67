# example of asyncio task group
import asyncio

# coroutine task
async def task1():
    # report a message
    print ('Hello from coroutine 1')
    # sleep to simulate wating 
    await asyncio.sleep(1)

# coroutine task
async def task2():
    # report a message
    print ('Hello from coroutine 2')
    # sleep to simulate wating 
    await asyncio.sleep(1)

# coroutine task
async def task3():
    # report a message
    print ('Hello from coroutine 3')
    # sleep to simulate wating 
    await asyncio.sleep(1)

# asyncio entry point
async def main():
    #create task group
    async with asyncio.TaskGroup() as group:
        # run first task
        t1 = group.create_task(task1())
        # run second task
        t2 = group.create_task(task2())
        # run third task
        t3 = group.create_task(task3())
        # wait a moment
        await asyncio.sleep(0.5)
        # cancle the second task
        t2.cancel()

    # check the status of each task
    print(f'Task1: done={t1.done()}, cancelled={t1.cancelled()}')
    print(f'Task2: done={t2.done()}, cancelled={t2.cancelled()}')
    print(f'Task3: done={t3.done()}, cancelled={t3.cancelled()}')
# entry point 
asyncio.run(main())