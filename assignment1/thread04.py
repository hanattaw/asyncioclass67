# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')
        # store return value
        self.value = 99

# create a thread
thraed = CustomThread()
# run the thread
thraed.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thraed.join()
# get the value returned from run
value = thraed.value
print(f'{ctime()} Got: {value}')