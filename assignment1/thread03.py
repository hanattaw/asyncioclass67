# extending the Thread class
from time import sleep, ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        sleep(1)
        print(f'{ctime()} this is coming from another thread')
        # store return value
        self.value = 99

thread = CustomThread()
thread.start()
print(f'{ctime()} waiting for the thread to finish')
thread.join()
# get the value returned from run
value = thread.value
print(f'{ctime()} Go: {value}')