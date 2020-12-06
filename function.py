# defining functions
print("-------------------defining a function----------------")
def calc(a, b):
    s = (a + b)
    m = a - b
    p = a * b
    d = a / b
    return s, m, p, d  # the result is returned to the function

# returned as tuple
result = calc(10, 20)  # calc function called and values are passed to the function
for i in result:
    print(i)


print("\n\n--------------Global and local variable--------------")
# global local variables
x = 123  # x is global variable can be accessed inside a function
def display():
    y = 678  # y is a local variable can't bve accessed outside the function
    x = 234
    print(globals()['x'])
    # 'globals()' function used to access the global variable value inside a function even though it contain same
    # named variable
    print(x, y)

# when executed the x is accessed from the global variable wherever called like in print function
# else if x is accessed using the function if any local variable value is defined that value is accessed
print(x)  # the global variable x is accessed
display()  # the x inside the function is accessed
z = display  # assigning the function to variable
z()  # directly invoke the function with variable and brackets


print("\n\n-------------function inside another function------------")

# function inside another function
def dis(name):
    def msg():  # defining a function inside a function
        return "hello "
    result = msg() + name  # appending the function with the variable input
    return result

print(dis("joe"))  # can't access the function that's inside the outside function
# i.e. can't access the function msg, the msg function will only be available inside the function dis


print("\n\n---------------function as parameter to another--------------")

def disp(fun):
    return "Hello " + fun
def name():
    return "Joe"

print(disp(name()))  # function is passed as parameter to another function


print("\n\n-----------------returning functions----------------")
# instead of returning the output of one function we can return the function itself
def displ():
    def message():
        return "hello"
    return message

func = displ()  # assigning a function's function to variable thus qwe=asd()
print(func())

# we can pass any data/sequence type to function
def lst(list):
    for i in list:
        print(i)
print("\n")
lst([1,2,3,'asd'])


print("\n\n--------------------recursion function------------------")
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


print("\n\n----------------keyword argument-------------------")
def avg(a=2,b=3):
    print("a=",a)
    print("b=",b)
    return (a+b)/2

print("values passed, ",avg(b=10,a=20)) # even though the argumnets in the function is deined as a,b
# we can pass it in our own way using keyword's argument no matter the series

print("default values used ", avg()) # even though no argument is passed the function uses the default values,
# if any values are passed in the argument it overrides the default values as seen above
