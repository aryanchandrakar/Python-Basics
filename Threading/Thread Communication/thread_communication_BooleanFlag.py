# real time applications which use multiple threads often these threads need to communicate with each other
# to get the job done and a very common pattern we see in multi-threaded application


# Thread needs to know when the work is available for processing , one way to do this communication is to have a
# flag, a boolean flag called orders placed on the producer thread, the consumer thread will be continuously checking
# if this flag is true. Initially this flag will be false only when the producer thread has a list of orders,
# it will be flipped this flag to true and the consumer thread will be continuously checking to see if this flag is true
# if it is true, then it will take the list of orders from the producer thread process them and ship them, so using a
# boolean flag is one way of thread communication.

# using Boolean flag
from threading import *
from time import sleep


class Producer:
    def __init__(self):
        self.products = []
        self.orderplaced = False

    def produce(self):
        for i in range(1, 5):
            self.products.append("Product" + str(i))
            sleep(1)
            print("Item added")
        self.orderplaced = True
        # turn the flag to true


class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        while self.prod.orderplaced == False:
            print("Waiting for producer")
            sleep(0.2)
        # the consumer thread running parallely check if the flag turns true until then it sleep
        # when it turn to true it take order and ship them

        print("Order Shipped", self.prod.products)


p = Producer()
c = Consumer(p)
t1 = Thread(target=p.produce())
t2 = Thread(target=c.consume())
t1.start()
t2.start()

