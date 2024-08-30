# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        #display message
        print(f'{ctime()} This is coming from another thread')
        # store return value
        self.value = 99

# create thread
thread = CustomThread()
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join()
# get the value returned from run
value = thread.value
print(f'{ctime()} Got: {value}')