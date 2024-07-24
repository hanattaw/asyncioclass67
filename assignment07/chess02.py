import time
import asyncio

my_compute_time = 0.1  # Judit's thinking time in seconds
opponent_compute_time = 0.5  # Opponent's thinking time in seconds
opponents = 24  # Number of opponents
move_pairs = 30  # Number of move pairs

async def game(x):
    # Loops 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} ({i+1}) Judit made a move.")
        
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} ({i+1}) Opponent made move.")
        
    print(f"BOARD-{x+1} >>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

async def main():
    start_time = time.perf_counter()
    board_time = 0
    # Create a list of game tasks
    tasks = [game(board) for board in range(opponents)]
    # Wait for all games to complete
    results = await asyncio.gather(*tasks)
    board_time = sum(results)
    
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

# Run the main function
asyncio.run(main())
