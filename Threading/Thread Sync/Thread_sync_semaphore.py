# SEMAPHORE
# Semaphore is simply acquiring a lock but internally it uses a counter. Internally, initially there will
# be a number 1 and every time a lock is acquired this number will be decremented by 1 which will be zero.
# And then once the lock is released, that is incremented by 1 again, everything else is same.

print("\n\n------------------SEMAPHORE-----------------")
# using LOCKs
from threading import *
from time import sleep
class BookMyBussec:
    def __init__(self,avaseat):
        self.avaseats=avaseat

        self.l=Semaphore() # Semaphore present in threading module


    def buytkt(self,seatsreq):

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

obj=BookMyBussec(10)
s1=Thread(target=obj.buytkt,args=(3,))
s2=Thread(target=obj.buytkt,args=(3,))
s1.start()
s2.start()


# will get similar results but we are locking the entire thread for entire single process so that no problem occur

