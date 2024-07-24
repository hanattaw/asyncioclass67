import time 

my_compute_time = 0.1
opponents_compute_time = 0.5
opponents = 3
move_pairs = 30

def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD- {x+1} {i+1} Judit made a move")
        time.sleep(opponents_compute_time)
        print(f"BOARD = {x+1} {i+1}- Opponent made move")
    print(f"BOARD-{x+1}- >>>>>>>>Finished move in {round(time.perf_counter() - board_start_time)} secs\n ")
    return round(time.perf_counter() - board_start_time)

if __name__== "__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(opponents):
        board_time += game(board)

    print(f"Board exhibitos finished in {board_time} sec.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs. ")