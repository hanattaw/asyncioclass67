# running a function in another thread

from threading import Thread
from time import sleep, ctime

#a custom function that blocks for moment
def task():
    #block for a moment
    sleep(1)
    #display a messge
    print(f'{ctime()} This is from another thread')

#create a thread
thread = Thread(target=task)
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
