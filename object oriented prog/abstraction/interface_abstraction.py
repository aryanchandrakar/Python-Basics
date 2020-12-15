# interface is simply a class with all method as abstract method

from abc import abstractmethod,ABC
class BMW(ABC): # for mandating all child class to implement abstract class
    # the abstract class "BMW" should inherit from class ABC

    # no interface or particular keyword to define an interface
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self): # abstract method contract, can pass other parameter here that must be in child class too
        pass # abstract class have no implementation, include pass is necessary

class Threeseries(BMW):
    def __init__(self, ccenabled, make, model,year):
        super().__init__(make, model, year)
        self.cruise = ccenabled
    def display(self):
         print(self.cruise)
    def start(self):
        super().start()
        print("button started")
    def stop(self):
        super().stop()
        print("button stopped")
    def drive(self): # all child class should implement abstract method
        print("Three series drive")

class Fiveseries(BMW):
    def __init__(self, paenabled, make, model,year):
        BMW.__init__(self, make, model, year)
        self.assist = paenabled
    def start(self):
        super().start()
        print("button started")
    def stop(self):
        super().stop()
        print("button stopped")
    def drive(self): # all child class should implement abstract method
        print("Five series drive")


# we cant initiate class BMW now it's an interface
threeseries=Threeseries(True,"BMW","12e","2018")
print(threeseries.cruise)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
threeseries.start()
threeseries.stop()
threeseries.display()

fiveseries=Fiveseries(True,"BMW","15w","2020")
print(fiveseries.assist)
print(fiveseries.make)
print(fiveseries.model)
print(fiveseries.year)
fiveseries.start()
fiveseries.stop()

# abstract method may not implement all method of parent class
