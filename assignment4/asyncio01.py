# example of getting the current task from the main coroutine
import asyncio

#define a main corotine
async def main():
    #report a massage
    print("main coroutine started")
    #get the current task
    task = asyncio.current_task()
    #report this detils
    print(task)

#start the aysncio program
asyncio.run(main())