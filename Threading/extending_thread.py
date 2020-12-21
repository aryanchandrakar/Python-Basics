print("\n\n----------------Extending thread class----------------")
# extending thread subclass
from threading import Thread
class Mythread(Thread): # extending class
    def run(self): # overriding run method from parent class
        i=0
        while (i <= 10):
           print(i)
           i += 1

th =Mythread()
th.start() # call run method, call start method it will start and internally it will spawn off a new thread
# and invoke run method.

print("\n\n-----------------Threading using a class--------------")
from threading import *
from time import sleep

class Mythread(Thread): # extending class
    def displayno(self): # overriding run method from parent class
        i=0
        print(current_thread().getName())
        sleep(1) # making thread sleep
        # thread 3 starts and goes to sleep for a sec while same time thread 4 starts and go to sleep
        # and same for thread5, then thread 3 starts executing and similarly other threads
        
        while (i <= 10):
           print(i)
           i += 1
obj=Mythread() # create object of class
t=Thread(target=obj.displayno) # pass instance of object as target to thread
t.start()
t1=Thread(target=obj.displayno) # pass instance of object as target to thread
t1.start()
t2=Thread(target=obj.displayno) # pass instance of object as target to thread
t2.start()

# The scheduling of these three threads is up to the Python thread scheduler
# Thread-1, it prints the numbers from 0 to say 4 and then Thread-2 starts off.
# So it depends on the Python thread scheduler how the scheduling happens.
# But all of them will do their work at the end.
