import asyncio
import time
my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} judit made a move.")
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move.")
    duration = round(time.perf_counter() - board_start_time)
    print(f"BOAED-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} sec\n")
    return duration

async def main():
    start_time = time.perf_counter()
    tasks = [game(board) for board in range(opponents)]
    results = await asyncio.gather(*tasks)
    board_time = sum(results)
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__":
    asyncio.run(main())
    
    