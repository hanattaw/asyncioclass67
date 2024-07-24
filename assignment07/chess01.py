import time
my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

def game(x):
    # Loops 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} judit made a move.")
        time.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move.")
    print(f"BOAED-{x+1} - >>>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} sec\n")
    return round(time.perf_counter() - board_start_time)


if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    # Loops 24 times because we are playing 24 opponents
    for board in range(opponents):
        board_time += game(board)
    
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")