import threading
import logging
import time

def thread_function(name, sleep_time):
    logging.info("Thread %s: starting", name)
    time.sleep(sleep_time)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, 
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info(f"Main     : create and start thread %d.", index)
        sleep_time = 4 if index == 1 else 2
        x = threading.Thread(target=thread_function, args=(index, sleep_time))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main    : before joining thread %d.", index)
        thread.join()
        logging.info(f"Main    : thread %d done", index)
