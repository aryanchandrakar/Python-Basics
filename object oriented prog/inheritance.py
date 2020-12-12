# By Inheritance(Is-A Relation) defining a new object with the help of existing object the new object might access
# the existing object functionalities and even have an update in those 2 similar objects properties can be re used
# while other object with lower similarity may have a relation to other object- re usablity an object IS A part of
# class like bmw IS A car - is-a relation
#
# Parent class
# class Parent :
#            # Constructor
#            # Variables of Parent class
#
#            # Methods
#
# # Child class inheriting Parent class
# class Child(Parent) :
#            # constructor of child class
#            # variables of child class
#            # methods of child class

#parent class
class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self): # parent class's functionality
        print("started")
    def stop(self): # parent class's functionality
        print("stoped")

# child class
class Threeseries(BMW):  # BMW is inherited in threeseries
    def __init__(self, ccenabled, make, model,year):  # all the fields of the parent class are inherited in the child class
        BMW.__init__(self, make, model, year)  # invoke parent class constructor
        super().__init__(make, model, year)  # super- to invoke parent class method and constructors from child class constructor and method
        self.cruise = ccenabled

    def display(self): # the child can also have their own functionality
         print(self.cruise) # this functionality is present only in the child class - three series
        # no other child class or parent class has this functionality

# OVERRIDING
# process of implementing same method that is present in the parent class in the child class    
    def start(self):  # overriding parent class functionality
        super().start() # invoking parent class method from child class method
        # help in executing parent class functionalities as well even though overridden
        print("button started")


class Fiveseries(BMW):  # BMW is inherited in threeseries
    def __init__(self, paenabled, make, model,year):  # all the fields of the parent class are inherited in the child class
        BMW.__init__(self, make, model, year)  # invoke parent class constructor
        self.assist = paenabled

# creating object of child class
threeseries=Threeseries(True,"BMW","12e","2018")
print(threeseries.cruise)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
# everything of the parent class is used in the child class - re usablity

# inheriting method/functionalities
threeseries.start() # the start functionality is overridden by the functionality of the child class
# thus the specification in the parent class functionalities no more matter the functions in the child class execute
threeseries.stop()
threeseries.display() # this functionality is present only in the child class - three series
# no other child class or parent class has this functionality
# the child can also have their own functionality


# super() - to invoke parent class method and constructors from child class constructor and method
