# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread


# A custom thread class
class CustomThread(Thread):
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print(f'{ctime()} This is from another thread')
        #store return value
        self.value = 99


# create a thread
thread = CustomThread()

#run the thread
thread.start()

#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()

#get the value returned from run
value = thread.value
print(f'{ctime()} Got: {value}')