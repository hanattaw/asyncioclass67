# Starting a Thread
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: Starting", name)
    time.sleep(2)
    logging.info("Thread %s: Finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.info("Main  : Before creating thread")
x = threading.Thread(target=thread_function, args=(1,))
logging.info("Main  : Before running thread")
x.start()
logging.info("Main  : Wait for the thread to finish")
# x.join()
logging.info("Main  : All done")