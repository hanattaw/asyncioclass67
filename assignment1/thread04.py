# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread

# Custom thread class
class CustomThread(Thread):
    # Override the run function
    def run(self):
        # Block for a moment
        sleep(1)
        # Display a message
        print(f'{ctime()} This is coming from another thread')
        # Store return value
        self.value = 99

# create a thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join()
# Get the value returned from run
value = thread.value
print(f'{ctime()} Got: {value}')