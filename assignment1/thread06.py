# Working With Many Threads
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


    threads = list()
    for index in range(3):
        logging.info("Main  : Create and start thread %d", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()


    for index, thread in enumerate(threads):
        logging.info("Main  : Before joining thread %d.", index)
        thread.join()
        logging.info("Main  : thread %d done", index)