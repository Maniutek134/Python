#!/usr/bin/python

import threading
import time
import threading

#brak death locka

def jedzenie(nr, widelce, lock):
    
    print ("start")
    count = 0
    
    if ((nr+1)%5 > nr):
        widelce[nr%5].acquire()
        time.sleep(5)
        widelce[(nr+1)%5].acquire()

    else:
        widelce[(nr+1)%5].acquire()
        time.sleep(5)
        widelce[nr%5].acquire()

    print ("jem")

    if ((nr+1)%5 > nr):
        widelce[(nr+1)%5].release()
        widelce[nr%5].release()
    else:
       widelce[nr%5].release()
       widelce[(nr+1)%5].release()
       
    print ("end")

widelce = []
for i in range(0,5):
    widelce.append(threading.Lock())
lock = threading.Lock()
threads=[]

class myThread(threading.Thread):
    def __init__(self, nr,widelce,lock):
        threading.Thread.__init__(self)
        self.widelce=widelce
        self.nr=nr
        self.lock=lock
    def run(self):
        jedzenie(self.nr,self.widelce,self.lock)

try:
    thread0=myThread(0,widelce,lock).start()
    thread1 =myThread(1,widelce,lock).start()
    thread2 =myThread(2,widelce,lock).start()
    thread3 =myThread(3, widelce, lock).start()
    thread4 =myThread(4, widelce, lock).start()



except:
   print ("Error: unable to start thread")

print ("koniec")