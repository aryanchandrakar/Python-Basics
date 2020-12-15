from abc import abstractmethod, ABC


class TouchscreenLap(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

# abstract method may not implement all methods of parent class/interface

class HP(TouchscreenLap):
    def __init__(self,make, model,):
        super().__init__(make, model)
    @abstractmethod
    def scroll(self):
        pass
class DELL(TouchscreenLap):
    def __init__(self,make, model,):
        super().__init__(make, model)
    @abstractmethod
    def scroll(self):
        pass

class HPnotebook(HP):
    def __init__(self,make,model):
        super().__init__(make,model)
    def click(self):
        print("Click enabled HP")
    def scroll(self): # overriding scroll cause abstract class can't be instantiated
        print("Scroll enabled HP")
class DELLnotebook(HP):
    def __init__(self,make,model):
        super().__init__(make,model)
    def click(self):
        print("Click enabled DELL")
    def scroll(self):
        print("Scroll enabled DELL")

hpnotebook=HPnotebook("HP","TouchscreenHP")
hpnotebook.click()
hpnotebook.scroll()

dellnotebook=DELLnotebook("DELL","TouchscreenDELL")
dellnotebook.click()
dellnotebook.scroll()
