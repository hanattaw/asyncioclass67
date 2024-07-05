# Working With Many Threads
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def thread_function4(name):
    logging.info("Thread %s: starting", name)
    time.sleep(4)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                         datefmt="%H:%M:%S")

    threads = list()
    time1 = time.time()
    for index in range(3):
        logging.info("Main  : create and start thread %d.", index)
        if index == 1:
            x = threading.Thread(target=thread_function4, args=(index,))
        else:
            x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main  : before joining thread %d.", index)
        thread.join()
        logging.info("Main  : thread %d done", index)
    time2 = time.time() - time1
    print(f'all done {time2:0.2f}')
