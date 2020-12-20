# epoch - start of time in sec
# ctime() - from the type module to get time
# datetime() - classes and objects from that data time module

import time, datetime

print("-----------------epoch time-----------------")
# all seconds from beginning of time as per the system
epochsec = time.time()
print(epochsec)  # gives second since the start of unix epoch time 1 jan 1970
t = time.ctime(epochsec)  # epoch time in proper time and date
print(t)

# DATETIME module can support many of the same operations, but provides a more object oriented set of types,
# and also has some limited support for time zones.
print("\n\n-----------------current date time-----------------")
dt = datetime.datetime.today()
print(dt)
print("formatted")
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current Time: {}:{}:{}'.format(dt.hour, dt.minute, dt.second))

print("now today it's: ")
from datetime import *

nt = datetime.now().date()  # gives only date of present day
print(nt)

print("\n\n------------------combining date and time----------------")
# combining date and time
from datetime import *

d = date(2018, 7, 21)
t = time(12, 45)
dt = datetime.combine(d, t)
print(dt)

print("\n\n-------------------sorting dates--------------------")
from datetime import date

ldates = []
d1 = date(2000, 12, 11)
d2 = date(2000, 12, 1)
d3 = date(2020, 12, 20)
d4 = date(2020, 12, 21)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)

ldates.sort()  # for sorting dates

for i in ldates:
    print(i)

print("\n\n---------------------sleep----------------------")
import time
from datetime import date

ldates = []
d1 = date(2000, 12, 11)
d2 = date(2000, 12, 1)
d3 = date(2020, 12, 20)
d4 = date(2020, 12, 21)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.sort()

time.sleep(3)  # sleep for n seconds

for i in ldates:
    time.sleep(1)
    print(i)

print("\n\n-----------------getting the execution time---------------")
import time
from datetime import date

Starttime = time.perf_counter()

ldates = []
d1 = date(2000, 12, 11)
d2 = date(2000, 12, 1)
d3 = date(2020, 12, 20)
d4 = date(2020, 12, 21)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.sort()

# time.sleep(3) # sleep for n seconds

for i in ldates:
    time.sleep(1)
    print(i)

Endtime = time.perf_counter()
print("Execution time: ", Endtime - Starttime)
