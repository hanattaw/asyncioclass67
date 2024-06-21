# Starting a Thread
import threading
import logging
import time

def thread_function(name, delay):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, 
                        datefmt="%H:%M:%S")

    logging.info("Main     : before creating threads")
    x = threading.Thread(target=thread_function, args=(1,))
    
    logging.info("Main     : before running threads")
    x.start()
    logging.info("Main: wait for the threads to finish")
    # x.join()
    logging.info("Main     : all done")
