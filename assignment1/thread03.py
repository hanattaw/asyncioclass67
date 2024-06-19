# extending the Thread class
from time import sleep, ctime
from threading import Thread

#a cutom function that blocks for a moment
class CustomThread(Thread):

    def run(self):

        sleep(1)

        print(f'{ctime()} This is coming from anther thread')

        self.value = 99

thread = CustomThread()

thread.start()

print(f'{ctime()} Waiting for the thread to finish')
thread.join()

value = thread.value
print(f'{ctime()} Got: {value}')