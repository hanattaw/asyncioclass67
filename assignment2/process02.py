# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources
# Multiprocessing 2 kitkens, 2 cooker, 2 dishes

# Share resources

import os
import multiprocessing
from time import sleep, ctime, time

# Basket of sharing

class Basket:
    def __init__(self):
        self.eggs = 50
    def use_eggs(self, index):
        print(f"{ctime()} Kitchen-{index} : Chef-{index} has lock with eggs remaining (self.eggs)")
        self.eggs -= 2
        print(f"{ctime()} Kitchen-{index} : Chef-{index} has released lock with eggs remaining (self.eggs)")

# Chef cooking

def cooking(index, basket):
    #chef use egs fos cooking
    basket.use_eggs(index)
    sleep(2)


# Kitchen cooking

def kitchen(index, share_eggs):
    print(f"{ctime()} Kitchen-{index} : Begin cooking... PID (os.getpid())")
    cooking_time = time()
    cooking(index, share_eggs)
    duration = time() - cooking_time
    print(f"{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds!)")
    

if __name__ == "__main__":

    # Begin of main thread
    print(f"{ctime()} Main : Start Cooking... PID (os.getpid())")
    start_time = time()

    basket = Basket()

    # Multi processes
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        # Starting processes
        p.start()
    

    # Wait until processes are finished
    for index, p in enumerate(kitchens):
        p.join()

    # End of main thread
    print(f"{ctime()} Main : Basket eggs remaining (basket.eggs)")
    duration = time() - start_time
    print(f"{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds)")
