# running a function in another thread
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task():

    sleep(5)

    print(f'{ctime()} This is from another thread')

thread = Thread(target=task)

thread.start()

print(f'{ctime()} Waiting for the thread...')
thread.join()