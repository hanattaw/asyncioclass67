# example of gather for many coroutines in a list
import asyncio

# coroutine used for a task
async def task_corou(value):
    # report a massage
    print(f"Task {value} executing")
    # sleep for a moment
    await asyncio.sleep(1)

# coroutine used for the entry point
async def main():
    # report a massage
    print("main Starting")
    # create many coroutines
    coros = [task_corou(i) for i in range(10)]
    #run the tasks
    await asyncio.gather(*coros)
    #report a massage
    print("main done")

# start the asyncio program
asyncio.run(main())