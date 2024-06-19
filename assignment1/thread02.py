# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

#a cutom function that blocks for a moment
def task(sleep_time, message):

    sleep(sleep_time)

    print(f'{ctime()} {message}')

thread = Thread(target=task, args=(1.5, 'New message from anorther thread'))

thread.start()

print(f'{ctime()} Waiting for the thread...')
thread.join()