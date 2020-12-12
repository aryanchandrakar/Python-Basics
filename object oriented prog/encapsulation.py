# protecting functionality and data of objects from other objects
# class{
# data
# code
# }

# private field
print("-------------private field-------------")
class Student:
    def __init__(self):
        # self.id=123
        self.__id=123 # as seen the difference,before the variable name we have "__" which mark them as private
        self.__nane="Joe"

    def display(self): # to access the private field we create a display function
        print(self.__id)
        print(self.__nane)
        # but we still can't display using object as s.id or s.name we do so by calling the funtion

s=Student() # as we made the variables private we can't create an object from it
# print(s.id) # we can't access the object as it's private now hidden
# print(s.name)
s.display()

# name mangling
print("\n\n---------------name mangling---------------")
# when we make variables or fields private they are not completely hidden
# instead they are stored as object._classname__variable/fieldname
print(s._Student__id)


# we see the private field are not completely hidden and can be accessed using different syntax
# implementing encapsulation using setter and getters
print("\n\n---------------encapsulation--------------")
class Stud:
    def setId(self,iid):
        self.iid=iid
    def getId(self):
        return self.iid
    def setName(self,nme):
        self.nme=nme
    def getName(self):
        return self.nme
s=Stud()
s.setId(123) # only way to set value no other way
s.setName("Joe")
print(s.getId())
print(s.getName())
