# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time

#Cooing synchonous
def cooking(index):
    print(f'{ctime()} Kitchen-{index}         : Begin cooking')
    sleep(2)
    print(f'{ctime()} Kitchen-{index}         : Cooking done')

if __name__=="__main__":
    #begin of main thread:
    print(f'{ctime()}Main              :Start Cooking')
    start_time = time()
    #cookinf
    cooking(0)

    duration = time() - start_time
    print(f"{ctime()}Main    :Finished cooking duration in {duration:0.2f} seconds")