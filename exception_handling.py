# while execution something goes wrong exception is raised
# if we don't handle it the program may terminate abruptly
                     # display of unfriendly exception information
                     # improper shutdown of resources
# we have exception class with predefined exception type or user defined type
# try: code
# except Exception: what to do
# else: to be executed in case of exception
# finally: clean up code
#
# each exception is a class and and object of that class is created when exception is raised
# parent of all these exception is the baseException which is inherited by a Exception class
# Exception class consist of StandardError and Warning
# example of StandardError - EOF error-end of file error when trying to read file beyond the end of file
#                          - ZeroDivisionError - when trying to divide by 0
#                          - IndentationError - improper indentation usage
# example of Warning - DeprecatedWarning - seen when trying to use python API- trying to use something that was there in older version and is now depricated use latest thingy
#                    - ImportWarning - when importing modules and not using them
# when we create our own exception handling it's inherited from the exception class

try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter 2 number: ").split()]
    c=a/b
    f.write("written %d in file" %c)
    print(c)
    #don't close the file here cause if exception occur the file won't be closed and except block will be executed
except ZeroDivisionError:
    print("Dividing by zero")
else: # executes when no exception is raised
    print("entered non 0 number")
finally: # to execute something no matter exception or not
    f.close()
    print("[+]file closed")
print("[\]okay bie bie!")

# creating and raising own exceptions
# extending the exception class and can add msg to constructor, such that msg will be rendered on UI when exception is raised
class OverlimitException(Exception):
    def __init__(self,msg):
        self.msg=msg
def withdrawl(amt):
    if(amt>500):
        raise OverlimitException("above limit withdrawl")
withdrawl(400)


# logging

import logging

# logging configuration
# to log this to a file and also configure the log level at the same time
# use logging.basicConfig(fileName.log,logLevel)
logging.basicConfig(filename="mylog.log",level=logging.ERROR) # only logs above this level is logged in file
# level specification in caps, it's log thus appended not overwritten

# different levels of log msg according to their levels
logging.critical("Critical")
logging.error("Error")
logging.warning("Warn") # warn is deprecated
logging.info("Info")
logging.debug("Debug")

# default log level is warning all the logs above it resulting in no output for logs after warning


# logging exception
import logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG) # only logs above this level is logged in file

try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter 2 number: ").split()]
    logging.info("Dividing") # logging information
    c=a/b
    f.write("written %d in file" %c)
    print(c)
    #don't close the file here cause if exception occur the file won't be closed and except block will be executed
except ZeroDivisionError:
    print("Dividing by zero")
    logging.error("Division by 0") # logging exception
else: # executes when no exception is raised
    print("entered non 0 number")
finally: # to execute something no matter exception or not
    f.close()
    print("[+]file closed")
print("[\]okay bie bie!")


# assertion
# assert returns boolean value "assert condition,exception_output"
# we can keep the code running after assertion exception using try and except
try:
    n=int(input("enter even number: "))
    assert n%2==0,"Entered odd!"
except AssertionError as ae:
    print(AssertionError)
    print(ae) # the exception_output in assert statement is printed and the code continues further
print("Bie!")
# if n%2==0 true is return and no output else exception is raised and following statement is printed
