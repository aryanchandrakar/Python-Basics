# abstract class and interface
# ABC class from abc module
# interfaces are abstract classes where all method are abstract

# we define an abstract method (has no implementation) in a parent class
# any child class that extend the parent class has to implement the abstract method
# if it doesn't abstract class will provide implementation for it and it will become an abstract class too
# we can have method in abstract class that can have implementation but one method in abstract class is abstract method
# if all method are not abstract then like usual can create instance of that class
# but if one method in class is abstract method then it becomes abstract class

# we define a contract in abstract class and all the child class has to fulfill and execute them
# with exact number of parameters and method signature exact same

from abc import abstractmethod,ABC
class BMW(ABC): # for mandating all child class to implement abstract class
    # the abstract class "BMW" should inherit from class ABC
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print("started")
    def stop(self):
        print("stoped")

    @abstractmethod
    def drive(self): # abstract method contract, can pass other parameter here that must be in child class too
        pass # abstract class have no implementation, include pass is necessary

class Threeseries(BMW):
    def __init__(self, ccenabled, make, model,year):
        BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.cruise = ccenabled
    def display(self):
         print(self.cruise)
    def start(self):
        super().start()
        print("button started")

    def drive(self): # all child class should implement abstract method
        print("Three series drive")

class Fiveseries(BMW):
    def __init__(self, paenabled, make, model,year):
        BMW.__init__(self, make, model, year)
        self.assist = paenabled

    def drive(self): # all child class should implement abstract method
        print("Five series drive")

bmw=Threeseries(True,"BMW","12e","2018") # any type of object can be assigned
print(bmw.cruise)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.display()
bmw=Fiveseries(True,"BMW","15w","2020") # method override
print(bmw.assist)
print(bmw.make)
print(bmw.model)
print(bmw.year)
bmw.start()
bmw.stop()

# abstract method may not implement all method of parent class
