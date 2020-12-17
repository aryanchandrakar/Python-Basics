# can be of many types binary img data
# file is opened as file_name=open("file_name.extension","mode","buffer")
# buffer is number passed that is used while reading a file while reading or writing the file.
# by default value of buffer is 4096 or 8092
# file_name.close() to close file

# write to file
f=open("myfile.txt","w")
s=input("enter text: ")
f.write(s)
f.close()


# check for file existence before reading
import os,sys  # os has isfile module return boolean true false if file exist or not
# sys has exit module to exit out if no file exist
if os.path.isfile('myfile.txt'):  # os.path.isfile('file_name.extension')
    f = open("myfile.txt", "r")  # if file exist open and continue to read file
else:
    print("File doesn't exist")  # if file doesn't exist exit the program
    sys.exit()

# read a file
s=f.read()
print("you wrote ",s)
f.close

# writing multiple strings
f=open("myfile.txt","w")
print("Enter Text (type # when you are done): ")
s=''
while s!='#':
    s=input()
    f.write(s)  # everything is written in one line
    f.write(s+"\n")  # everything written as input with proper line ends
f.close()


# PICKLE writing an object to a stream
# serialize an OBJECT in to a file
import pickle
class Student:
    def __init__(self,id,name,testscore):
        self.id=id
        self.name=name
        self.testscr=testscore
    def display(self):
        print(self.id,self.name,self.testscr)

f=open("Student.dat","wb")
s=Student(123,"Joe",45)
pickle.dump(s,f)  # 2 parameters the object we wanna dump, file we want to dump in
f.close()


# unpickle
import pickle
f=open("Student.dat","rb")
o=pickle.load(f)  # parameter is the file that we opened - TO UNPICKLE
o.display()
f.close()
