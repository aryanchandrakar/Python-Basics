from threading import *
from time import sleep


class BookMyBus:
    def __init__(self,avaseat):
        self.avaseats=avaseat
    def buy(self,seatsreq):
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

obj=BookMyBus(10)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(3,))
t1.start()
t2.start()
# both starts same time thus processing appears together like in previous file printing 1 to 10

# There's an issue refer thread_sync_lock.py
