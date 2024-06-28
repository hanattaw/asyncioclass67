# Thread version of cooking 1 kitchen 1 chefs 1 dishes
import os
from time import sleep, ctime, time
import threading 

def cooking(index, basket):
    print(f'{ctime()} Kitchen-{index}      : Begin Cooking...PID {os.getpid()}')
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index}      : Begin Cooking.')
    sleep(2)
    duration = time() - cooking_time
    basket.use_eggs(index)
    print(f'{ctime()} Kitchen-{index}      : Cookeing done in {duration:0.2f} seconds!')

class Basket:
    def __init__(self) -> None:
        self.eggs = 50
        self._lock = threading.Lock()
    def use_eggs(self, index):
        with self._lock:
            print(f'{ctime()} Kitchen-{index}   : Chef-{index} has lock with eggs remaining {self.eggs}')
            self.eggs -= 1
            print(f'{ctime()} Kitchen-{index}   : Chef-{index} has released lock with eggs remaining {self.eggs}')

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main      : Starting Cook.')
    start_time = time()

    basket = Basket()

    print(f'{ctime()} Main      : ID of main process: {os.getpid()}')
    
    # Multi thread cookingin 
    chefs = list()
    for index in range(2):
        c = threading.Thread(target=cooking, args=(index, basket))
        chefs.append(c)
        c.start()

    for index, c in enumerate(chefs):
        c.join()

    print(f'{ctime()} Main      : Basket eggs remaining  {basket.eggs} seconds!')
    duration = time() - start_time
    print(f'{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds')