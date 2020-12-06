# lambda argument_list:expression
# lambda always return a function which needs to be invoked when accessed
# f= lambda x:x*x # result=f(10) lambda return a squaring function
# which gets invoked by passing value to function f

print("--------------lambda single argument--------------")
# def cube(n):
#     return n**3
# print(cube(2))

f=lambda n:n**3 # n hold the body result of the body lambda "n" : body and assigned it to variable f
print(f(2))

print("\n\n--------------------if else lambda----------------")
l=lambda x: 'YES' if x%2==0 else 'NO'
# return statement1 if condition else return statement2
print(l(10))

print("\n\n---------------lambda with multiple argument-----------")
# function to add numbers

# def add(a,b):
#   return a+b
# print(add(10,20))

# lambda function for same
l= lambda a,b:a+b
print(l(10,20))

print("\n\n-----------------filter function lambda----------------")
lst=[10,25,20,34,65]

# filter function to filter the content of the input set
# filter(condition of filter on every expression, input for condition) returns filter object
# filter object as the memory location, thus converted to list type
rslt =list(filter(lambda x:x%2==0,lst))
print(rslt)

print("\n\n-----------------map function lambda-----------------")

# map function to manipulate the content of the input set
# map(function to be performed, input set) return manipulated input set
# same as filter map return object location use type conversion to get the output
rslt = list(map(lambda n:n*2,lst)) # map function use the lambda function against each
# expression in the list to return manipulated output as list back
print(rslt)

print("\n\n-----------------reduce function lambda-----------------")
# reduce function not available directly, need to import from functools
from functools import reduce
# reduce(function, sequence)
rslt = reduce(lambda x,y:x+y, lst)
# we get the result back as a single result not a sequence, thus do not gives object location, direct result
# no need of type conversion
print(rslt)
