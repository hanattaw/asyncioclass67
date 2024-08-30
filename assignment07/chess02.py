import time
import asyncio

my_computer_time = 0.1
opponent_computer_time = 0.5
oppenents = 14
move = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(1,move+1):
        time.sleep(my_computer_time)
        print(f"Board {x} {i} Judit time move")
        await asyncio.sleep(opponent_computer_time)
        print(f"Board {x} {i} oppenent time move")
    print(f"Board - {x} >>>>>>>>> Finish move in {round(time.perf_counter() - board_start_time)}sec \n")
    return round(time.perf_counter() - board_start_time)

# main coroutine
async def main():
    coros = [game(i) for i in range(1, oppenents+1)]
    # run the tasks
    await asyncio.gather(*coros)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")