import time

my_computer_time = 0.1
opponent_computer_time = 0.5
oppenents = 3
move = 30

def game(x):
    board_start_time = time.perf_counter()
    for i in range(1,move+1):
        time.sleep(my_computer_time)
        print(f"Board {x} {i} Judit time move")
        time.sleep(opponent_computer_time)
        print(f"Board {x} {i} oppenent time move")
    print(f"Board - {x} >>>>>>>>> Finish move in {round(time.perf_counter() - board_start_time)}sec \n")
    return round(time.perf_counter() - board_start_time)


if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(1,oppenents+1):
        board_time += game(board)
    print(f"Board exhibition finished in {board_time} sec.")
    print(f"Finish in {round(time.perf_counter() - start_time)} secs.")