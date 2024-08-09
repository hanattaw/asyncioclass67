import time
import asyncio

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

#Again notice that i declare the main() funtion as a async function
async def main(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        #print(f"BOARD-{x+i} {i+1} just made a move.")
        #Don't use time.sleep() in an async function. I'm using it because in reality you ares't thinking.
        #move on 24 boards at the same time 
        time.sleep(my_compute_time)
        print(f"BOARD-{x+i} {i+1} just made a move.")
        #
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+i} {i+1} Opponent just made move.")
    print(f"BOARD-{x+i} - >>>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    #
    task = []
    for i in range(opponents):
        task += [main(i)]
    await asyncio.gather(*task)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")