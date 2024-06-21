# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

# custom function that blocks for a moment
def task(sleep_time, message):
    sleep(sleep_time)
    print(f'{ctime()} {message}')

# create thread
thread = Thread(target = task, args = {1.5, 'New message from another thread'})
# run thread
thread.start()

#wait for the thread to finish
print(f'{ctime()} waiting for the thread...')
thread.join()