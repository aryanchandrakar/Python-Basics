# PRINT statments
print()
print("hi" * 3)
print("asdasd\nasdasd")
name = "joey"
marks = 40.543
print(name, marks, sep='----')  # sep used as the seperation between the printed elements
print("name ", name, " marks ", marks)  # printing as usual
print("name %s, marks %f" % (name, marks))  # print using the %
print("name %s, marks %0.2f" % (name, marks))  # the place values after decimal displayed on wish
print("name {}, marks {}".format(name, marks))  # using string format to display the string
print("name {1}, marks {0}".format(marks,
                                   name))  # indexing the format such that even not in sequence the print is correct

# INPUT function takes input as string bydefault
i = input()  # by default considered as string even though input is integer
j = int(input("enter intg! "))  # type casting the input
n = input("name? ")  # providing with context of the question
print(i, j, n)

# for string
lst = [x for x in input("enter number seperated by comma").split(',')]  # multiple inputs
# for integer lst=[int(x) for x in input("enter number seperated by comma").split(',')] # multiple inputs
# .split("the seperator specified")
print(lst)
