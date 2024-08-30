# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time

# Cooking Synchronous
def cooking(index):
    print(f'{ctime()} Kitchen-{index}   : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index}   : Cooking done!')

if __name__ == "__main__":
    # Begin main thread
    print(f'{ctime()} Main   : Start cooking...')
    start_time = time()
    # Cooking

    duration = time() - start_time
    print(f'{ctime()} Main   : Finished Cooking duration in {duration:0.2f} seconds')