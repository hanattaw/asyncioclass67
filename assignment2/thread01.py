# Thread version of cooking 1 kitchen 1 chefs 1 dishes
from time import sleep, ctime, time
from threading import Thread

def cooking(index):
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index}      : Begin Cooking.')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index}      : Cookeing done in {duration:0.2f} seconds!')

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main      : Start Cooking.')
    start_time = time()
    
    # Thread cooking
    index = 1 
    c1 = Thread(target=cooking(index))
    c1.start()
    c1.join()

    duration = time() - start_time
    print(f'{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds')
    