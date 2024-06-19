# running a function in another thread
from time import sleep, ctime
from threading import Thread

#a custom function that block for a moment
def task():
    #block for a moment
    sleep(1)
    #display a massage
    print(f"Task done at {ctime()}")

#create a thread
Thread = Thread(target=task)
#run the thread 
Thread.start()
#wait for the thread to finish
print(f'{ctime()} witting for the thread...')
Thread.join()