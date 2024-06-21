# running a function with arguments in another thread
from threading import Thread
from time import sleep, ctime

# a custom function that blocks for a moment


def task(sleep_time, message):
    #block for a moment   
    sleep(sleep_time) 
    # display a message
    print(f'{ctime()} {message}')

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))

# run the thread
thread.start()

#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()