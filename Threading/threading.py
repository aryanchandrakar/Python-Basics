# Python virtual machine behind the scenes uses a thread called the main thread to execute the code which we have
# written. If we do not have any other threads,if you are not creating any other threads in our application except
# the main thread, then they are called single threaded applications.
#
# To make the best use of the underlying processor and to improve the performance of our application, we can create
# multiple threads that can execute in parallel. Making the best use of the processor and also our application will
# give the best user experience, it will be very fast.

# can be done by using Thread function, Extending thread class and overriding run,
# hybrid approach-w/o extending thread class


# main thread
import threading

print("------------------main thread------------------")

# getting current thread
print("Current thread that is running:", threading.current_thread().getName())

# comparing thread
if threading.current_thread() == threading.main_thread():
    print("Main thread")
else:
    print("Some other thread")

print("\n\n------------------function thread----------------")
# creating thread using functions
from threading import *

def displayno():
    i = 0
    print(current_thread().getName()) # this thread created when executing the function
    while (i <= 10):
        print(i)
        i += 1

print(current_thread().getName())
t = Thread(target=displayno) # this no main thread instead a new thread made by us
t.start()

