# it is quite possible that the first thread comes in, it does this if check and it sees that the seats are available
# and it goes in and it's going to confirm the seat, process the payment, etc. And just before the first thread does
# this reduction of availableSeats, the second thread can come in into this depending on how the thread scheduler
# schedules it. It can come in, does this check and it can see that the seats are still available. And it goes in and
# it can do the processing even when there are no seats available because the reduction has not happened. The second
# thread or the third thread can think that the seats are available, which is not a good thing.


# When multiple threads are accessing the same resources it is very important that they don't corrupt
# each other's resources or objects.
# We can do by locking an object for a particular thread using two different ways, using locks or semaphores.

# LOCK
# when a thread locks an object it enters into a room of its own. It will take that
# object and it will own that object and only when that thread releases that object the other threads can use that
# object or resource.
# This process of thread acquiring a lock and entering a room is also known as threat mutex.
# until we release the lock no other thread can use that locked object

print("---------------------LOCKS--------------------")
# using LOCKs
from threading import *
from time import sleep
class BookMyBus:
    def __init__(self,avaseat):
        self.avaseats=avaseat

        self.l=Lock() # lock present in threading module


    def buy(self,seatsreq):

        # to acquire a lock
        self.l.acquire()

        print("Total seats available: ", self.avaseats)
        if(seatsreq<=self.avaseats):
            print("Wait for confirmation")
            sleep(1)
            print("Processing")
            sleep(1)
            print("Processing")
            sleep(1)
            print("Processing")
            print("Processing the seats")
            print("Please print the ticket")
            self.avaseats-=seatsreq
        else:
            print("Processing")
            sleep(1)
            print("You are late sorry!")

        # to release a lock
        self.l.release()

obj=BookMyBus(10)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(3,))
t1.start()
t2.start()

# will get similar results but we are locking the entire thread for entire single process so that no problem occur
