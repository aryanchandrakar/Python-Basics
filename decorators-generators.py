# decorator perform additional logic on the function,
# takes in a function and return a function
# takes the function invokes it, get the output and perform additional function on it.
print("-------------double decorator---------")
def decor(fun):  # takes another function as parameter and return another function-inner function
    def inner():
        rslt = fun()
        return rslt * 2
    return inner

# to apply a decorator always to function we can do that by using @ simply
# same name as the decorator function "@decorator_function_name"
@decor  # once we use this we don't need line17,18 can direct invoke function line19
def num():
    return 5

# rsltfun=decor(num) # when the function is passed as parameter to another function no brackets needed
# print(rsltfun()) # when invoking a function we add brackets after specifying the function,
print(num())

print("\n\n-------------string decorator---------")
def hello(name):
    def howu(n): # parameter is passed to the function cause we take input in the main function
# if the return was direct in main function--"helloe joe",
# no parameter would have been needed to be passed in the decorator's inner function
                                    # see 36-45
        rslt=str(name(n))+" how are you!"
        return rslt
    return howu

@hello
def name(nme):
    return "hello "+nme
print(name("joe"))

# def hello(name):
#     def howu(): # parameter is passed to the function cause we take input in the main function
#         rslt=str(name())+" how are you!"
#         return rslt
#     return howu
#
# @hello
# def name():
#     return "hello joe"
# print(name())



# GENERATORS
# generators returns a sequence of values using yield statement
# help in creating custom sequences without storing the sequence in the memory
def customgen(x,y):
    while x<y:
        yield x
        x+=1
rslt=customgen(10,20)
for i in rslt:print(i)
