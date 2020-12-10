# class help in creating own datatype, like a blue print helping in creating anynumber of similar objects
# the objects will have same functionality with different values
# course name start with caps
print("--------------Class and objects-------------")
class Prod:
    def __init__(self): # self points to current object being created, the memory location
        self.name='Phone'
        self.description='okay'
        self.price=700
p1=Prod() # create object
# p1 is assigned to the current location of the self creating a dynamic field and assigning them the values
# self is the current object thus it would be p1.name, p1.description....
print(p1.name,p1.price,p1.description)


# using parameterized constructors
print("\n\n---------------constructors parameterized-------------- ")
class Course:
    def __init__(self,name,rating): # whatever is passed to the parameter
        self.name=name # is assigned to this object being created
        self.rate=rating

    # defining instance method
    def avg(self):
        norating=len(self.rate)
        avg=sum(self.rate)/norating
        print("avg rating- ", avg)

c1=Course("Joe",[1,2,3,4]) # self is passed itself to the object, need to pass the other parameter
c2=Course("John",[1,2,3,4])
print(c1.name,c1.rate)
c1.avg()
print(c2.name,c2.rate) # any number of objects can be created from a single class
c2.avg()


# getter setter method
print("\n\n-------------getter setter method--------------")
class Prog:
    def setName(self,n):
        self.name=n
    def getName(self): # no parameter in get
        return self.name
    def setSalary(self,sal):
        self.salary=sal
    def getSalary(self):
        return self.salary
    def setTech(self,tech):
        self.techno=tech
    def getTech(self):
        return self.techno
p1=Prog()
p1.setName("JOE")
p1.setSalary(100000)
p1.setTech(["Java","Python"])
print(p1.getName())
print(p1.getSalary())
print(p1.getTech())


# instance method
# Instance method are methods which require an object of its class to be created before
# it can be called. To invoke a instance method, we have to create an Object of the class in
# within which it defined.

# class contain the code to execute and only the output is returned when object function is called
print("\n\n-----------------instance method----------------")
class Produ:
    def __init__(self): # self points to current object being created
        self.name='Phone' # instance variable
        self.description='okay' # all variable defined inside the function, having their own instances
        self.price=700 # instance var not common for whole class, only in functions
    def display(self):
        print(self.name,self.price,self.description)

p1=Produ() # create object
p1.display() # no need to pass parameter
# p1 is assigned to the current location of the self creating a dynamic field and assigning them the values
# self is the current object thus it would be p1.name, p1.description....


# static field
print("\n\n------------------static field--------------------")
class Stud:
    major = "CSE" # static field, common for entire class, all functions
    def __init__(self,rol,name):
        self.rolno=rol # instance field
        self.name=name
s1=Stud(1,"Joe")
s2=Stud(2,"John")
print(s1.major,s1.rolno,s1.name) # instance field different for both object as per defined
print(s2.major,s2.rolno,s2.name) # major static field same for both objects
print(Stud.major) # can access the static field directly using the class, no need of objects

# static method
# They do not require a class instance creation. So, they are not dependent on the state of the object.
# Static method knows nothing about the class and just deals with the parameters.
print("\n\n---------------static method----------------")
class Objcont:
    numberofobj=0
    def __init__(self):
        Objcont.numberofobj+=1

    # defining static method as "@staticmethod"
    @staticmethod
    def displaycont():
        print(Objcont.numberofobj)
o1=Objcont()
o2=Objcont()
# everytime we create an object static field is created
Objcont.displaycont() # then we invoke static method which display count


# inner class
print("\n\n---------------inner class----------------")
class Car:
    def __init__(self,make,year):
        self.mke=make
        self.yr=year
    class Engine: # inner class
        def __init__(self,number):
            self.no=number
        def start(self):
            print("Engine started")
c=Car('BMW',2017) # creating instance of outer class
e=c.Engine(123) # creating instance of the inner class using object of the outer class
e.start()

