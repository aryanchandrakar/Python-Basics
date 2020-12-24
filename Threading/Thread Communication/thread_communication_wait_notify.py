# WAIT NOTIFY
# threads to communicate is to use the multi-threading API methods such as a wait, notify and notifyAll.
# So these methods are available on a class called Condition from the multi-threading API in Python.
# And once you use the Condition class in the producer you can access this Condition, that Condition object
# in your consumer and invoke the wait method.
# Instead of polling like earlier, inside a loop we were continuously checking for a flag earlier within the Consumer.

# So getting rid of the boolean flag, we are now going to use the Condition object inside the Producer and the
# Consumer will invoke the wait method and the producer should invoke the notify method whenever the orders are ready
# to be shipped. And there is also a notifyAll method. If multiple threads are waiting for the Producer to get its
# job done, then the Producer will invoke the notifyAll and all the threads waiting on the Producer will be notified
# and they can do their job at that point. But all this should happen in a lock context.
# That is, these threads should acquire the lock on this Condition object when they are working with them and only
# then they should use the wait, notify and notifyAll.
from threading import *
from time import sleep


class Producer:
    def __init__(self):
        self.products = []
        self.c=Condition() # to communicate between threads

    def produce(self):
        self.c.acquire() # acquire the lock
        for i in range(1, 5):
            self.products.append("Product" + str(i))
            sleep(1)
            print("Item added")
        self.c.notify() # will notify the lock waiting on the other thread
        self.c.release() # releasing the lock after notifying


class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        # to do everything in a synchronised context
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0) # how much time to wait after the notification happens before executing logic
        self.prod.c.release()
        print("Order Shipped", self.prod.products)


p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce())
t2 = Thread(target=c.consume())
t1.start()
t2.start()
