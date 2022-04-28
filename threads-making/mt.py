import threading
import time
import copy

""" very simple thread making ti only write whe counter every 3 sec"""

class ThreadCounter:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()
    
    def count(self,thread_num):
        while True:
            self.lock.acquire()
            self.counter += 3
            self.lock.release()

            txt = str("proccess num "+str(thread_num)+" equals " +str(self.counter))
            time.sleep(3)
            print(txt)


tc = [ThreadCounter(),ThreadCounter(),ThreadCounter(),ThreadCounter(),ThreadCounter(),ThreadCounter()]
t = []
for i in range(5):
    print(t)
    t.append( threading.Thread(target=tc[i].count, args=(i,)))
    t[-1].start()