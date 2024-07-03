# example of starting many tasks and getting access to all tasks
import asyncio

# coroutine for a task
async def task__coroutine(value):
    # report a message
    print(f'task {value} is running')
    # block for a moment
    await asyncio.sleep(1)

# definea main coroutine
async def main():
    # report a meassage
    print('main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task__coroutine(i)) for i in range(10)]
    # allow some of the task time to start
    tasks = asyncio.sleep(0.1)
    # get all tasks
    tasks = asyncio.all_tasks()
    # report all tasks
    for task in tasks:
        print(f'> {task.get_name()}, {task.get_coro()}')
        # wait for all tasks to complete
        await task

# started the asyncio program
asyncio.run(main())