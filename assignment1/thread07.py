# Using a ThreadPoolExecutor
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

    with concurrent.futures.ThreadPoolExecutor(max_worker=3) as executor:
        executor.map(thread_function, range(3))