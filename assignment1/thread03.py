# extending the Thread class
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

# create a thread
thraed = CustomThread()
# run the thread
thraed.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thraed.join()