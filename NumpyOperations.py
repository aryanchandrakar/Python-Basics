# import numpy as np
from numpy import *


# giving fix values

# arr=np.array([1,2,3,4,5])
arr=array([1,2,3,4,5])
brr=array([1,2,3,4,5],int) # specifies that the array has only  one type of value
crr=array(['a','s','d','e'])
print(arr)
print(brr)
print(crr)


# array store calculated values
# LINSPACE
ls=linspace(0,100,20) # takes three parameters and it says returns evenly spaced numbers over a specified interval.
print(ls) # will divide 0 to 100 into equal values such that we get 20 values --> by default 3rd value is 50 division

# LOGSPACE
lg=logspace(1,20) # very similar to line space. The only difference is it calculates the logarithmic value.
print(lg)

# RANGE
ar=arange(1,20,2) # similar to range but comes in array. same(start,end,steps) values
print(ar)

# ZEROES
z=zeros(20) # give array filled with only 0
print(z)

# ONES
o=ones(20)
print(o)
print(ones((2,3),int)) # a 2x3 dim array with all int 1


# MATH FUNCTIONS
# adding two array without using loops
a1=array([1,2,3,4,5])
b1=array([2,3,4,5,6])
print(a1+b1)
print(a1-2)
print(sin(a1)) # sin of all values
print(log(a1)) # log of all values
print(mean(a1)) # mean of all values
print(abs(a1)) # absolute values
print(min(a1)) # min of all the values
print(sum(a1)) # sum of all the values


# COMPARING ARRAYS
a2=array([10,30,50,70])
b2=array([20,10,60,80])
print(a2>b2) # compares it, return true or false accordingly
print(a2>=b2) # compares it, return true or false accordingly
print(a2<b2) # compares it, return true or false accordingly
print(any(a2>b2)) # if anyone of the values in the array satisfies, return would be true
print(all(a2>b2)) # if all of the values in the array satisfies, return would be true


# LOGICAL OPERATION
la=logical_and(a2>20,a2<200) # find if the array's value comes True/False and apply logical and on it
lo=logical_or(a2>20,a2<200)
print(la,lo)


# WHERE FUNCTION
print(where(a2==30,a2,0)) # if condition satisfy return a2 else 0
print(where(a2>b2,a2,b2)) # if condition satisfy return a2 else b2


# ARRAY COPYING
# shallow copy
a1=arange(1,10)
a2=a1.view()
a3=a1.copy()
print('a1',a1)
print('a2',a2)
print('a3',a3)
a2[3]=40  # shallow copy a change in one changes other too
a3[4]=50  # copy won't change in the other
print("after modification")
print('a1',a1)
print('a2',a2)
print('a3',a3)


# SLICING
a1=arange(3,12)
print(a1)
print(a1[3:7]) # slice the a1 array from index 3 to 7-1
print(a1[1:9:2]) # slicing with steps


# MULTIDIMENSIONAL ARRAY
a1=array([1,2,3,4,5])
a2=array([[1,2,3],[3,4,5]]) # 2D array
a3=array([[[1,2],[2,3],[3,4]]]) # 3D array
print(a2)
print(a3)
print(a1.ndim)
print(a2.ndim) # type of array, dimensional
print(a3.ndim)

print(a1.shape)
print(a2.shape) # dimension of array -- row,column
print(a3.shape)

# wanna change the dimension of the array
a2.shape=(3,2)
print(a2) # automatically changes from dim(2,3) to (3,2)

print(a1.size) # gives total size of array -- number of elements
print(a2.size)
print(a3.size)

print(a1.itemsize) # size of each element in array -- bytes, each int 8 bytes
print(a2.itemsize)
print(a3.itemsize)

print(a1.dtype) # data type of each element
print(a2.dtype)
print(a3.dtype)

print(a1.nbytes)  # total number of bytes required for the array 5* 8bytes
print(a2.nbytes)
print(a3.nbytes)


# RESHAPING ARRAY
q1=arange(12) # pdt of dim 1*12
print('q1',q1)

q2= reshape(q1,(2,6)) # reshape 1 dim array to 2 dim, the product of dimension must be equal -- 2*6=1*12
print(q2)
q3=reshape(q1,(2,3,2))
print(q3)

print(q3.flatten()) # convert multi dim to single dim array

print(eye(3)) # a 3x3 dim matrix with diag. element as 1



# https://numpy.org/doc/1.19/ refer here for more related topics on numpy
