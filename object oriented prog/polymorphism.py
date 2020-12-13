# poly morphic - multi behaviour
# polymorphism can be implemented using duck typing, dependency injection, +-overloading, method overriding

# Duck Typing
# not usually offered by the programming language but can be used if it's dynamic programming language
print("-----------------Duck Typing--------------")
class Dog:
    def talk(self):
        print("Bark")
class Human:
    def talk(self):
        print("Hello")

def callTalk(obj):
    obj.talk(); # dynamically invoke the talk method depending on what object we have
d= Dog()
callTalk(d)
h=Human()
callTalk(h)

# using duck typing here form of polymorphism
# cause the same function can do multiple things depending on what we do at run time


# Dependency Injection
# injecting an object into another object
print("\n\n-----------------Dependency Injection----------------")
class Flight:
    def __init__(self,engine):
        self.engine=engine # dependency injection
    def startengine(self):
        self.engine.start();
class AirBusEngine:
    def start(self):
        print("Starting Airbus engine")
class BoingEngine:
    def start(self):
        print("Starting Boing engine")

ae=AirBusEngine()
f=Flight(ae)
f.startengine()

be=BoingEngine()
f1=Flight(be)
f1.startengine()


# operator loading +
print("\n\n-----------------operator overloading-----------------")
x=10
y=20
s1="Hello"
s2=" Joe"
l1=[1,"abc",2]
l2=[3,"def",4]
print(x+y,s1+s2,l1+l2) # "+" operator is overloaded


#runtime polymorphism - method overriding
print("\n\n-----------------method overriding----------------")
class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print("started")
    def stop(self):
        print("stoped")
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
class Fiveseries(BMW):
    def __init__(self, paenabled, make, model,year):
        BMW.__init__(self, make, model, year)
        self.assist = paenabled

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
