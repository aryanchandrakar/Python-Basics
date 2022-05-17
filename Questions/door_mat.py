"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
import math

x,y=input().split()
mid=math.ceil(int(x)/2)
design=mid-1

# upper half
for i in range(1,design+1): # 1,2,3
    undersco=int(y)-(3*((i*2)-1)) 
    des=i*2-1
    print((int(undersco/2)*"-")+(des*".|.") +(int(undersco/2)*"-"))

# WELCOME
print((int((int(y)-7)/2)*"-")+"WELCOME"+(int((int(y)-7)/2)*"-"))

# Lower half
for i in range(design,0,-1): 
    undersco=int(y)-(3*((i*2)-1)) 
    des=i*2-1
    print((int(undersco/2)*"-")+(des*".|.") +(int(undersco/2)*"-"))


################## OR ####################


# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=(input()).split()
n=int(n)
m=int(m)    
for i,j in zip(range(int((m-3)/2),0,-3), range(1,n-1,2)):
    print(("-"*i)+(".|."*(j))+("-"*i))
x=int((3*n-7)/2)
print(("-"*x)+"WELCOME"+("-"*x))
for i,j in zip(range(3,int((m-3)/2+1),3), range(n-2,0,-2)):
    print(("-"*i)+(".|."*(j))+("-"*i))
