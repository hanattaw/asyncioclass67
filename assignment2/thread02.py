# Thread version of cooking 1 kitchen 1 chefs 1 dishes
import os
from time import sleep, ctime, time
from threading import Thread

def cooking(index):
    print(f'{ctime()} Kitchen-{index}      : Begin Cooking...PID {os.getpid()}')
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index}      : Begin Cooking.')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index}      : Cookeing done in {duration:0.2f} seconds!')

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main      : Starting Cook.')
    start_time = time()
    print(f'{ctime()} Main      : ID of main process: {os.getpid()}')
    
    # Multi thread cookingin 
    chefs = list()
    for index in range(2):
        c = Thread(target=cooking, args=(index,))
        chefs.append(c)
        c.start()

    for index, c in enumerate(chefs):
        c.join()

    duration = time() - start_time
    print(f'{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds')
    