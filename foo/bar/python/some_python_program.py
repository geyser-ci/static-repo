# Threading example
import time, thread


class CitySuggestQuery:
    def new(self, *args, **kwargs):
        pass
    

def myfunction(string, sleeptime, lock, *args):
    while True:
        lock.acquire()
        time.sleep(sleeptime)
        lock.release()
        time.sleep(sleeptime)

if __name__ == "__main__":
    lock = thread.allocate_lock()
    thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
    thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))
    CitySuggestQuery.new(123456789)

