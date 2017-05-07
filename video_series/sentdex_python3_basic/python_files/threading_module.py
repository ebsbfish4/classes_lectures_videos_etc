#! python3

# Python is linear. What this means is that the code executes in linear time,
# but of course it is nice to sometimes do multiple things at once and use more of your
# processing power. This is where threading comes in.

# The idea of threading is that you can perform multiple tasks at the same time.
# However, threading will not work if you are sharing the same variable in both
# of the threads. 

# The idea of a lock is that when you put it on a variable, when a function tries
# to access the object it locks and nothing else from another thread can access it
# at all until the previous thread has finished modifying it. THIS IS ABSOLUTELY
# NECCESSARY IF YOU ARE USING THREADS WITH SHARED VARIABLES. If two functions call
# print, for example, they can jumble up the messages.

# This program would take about 10 seconds running linearly, but took only
# 1.2 seconds with threading.

import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)
    with print_lock: # How you use the lock we created
        print(threading.current_thread().name, worker)

def threader():
    while True: # This means run until the main thread dies
        worker = q.get()
        exampleJob(worker)
        q.task_done()


q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True # It will die when the main thread dies
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()
print('Entire job took:',time.time() - start)
