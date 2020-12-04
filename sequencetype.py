# list, set, dictionary etc
# to define single element in tuple or list use "," after the element in the bracket -- [10,] ; (10,)

# LIST DATATYPE
print("\n\n------------------------LIST--------------------------")
l = [10, 20, "abc"]  # defining list
print(l, l[1], l[1:2])  # indexing, slicing
print(l * 4)  # repeat same list 4 times
print(len(l))  # length of list

l.append(40)  # adding a value to list
l.remove("abc")  # remove specified content from the list
del (l[1])  # delete the term at the index
print(l)
print(max(l), min(l))  # max and min value from the list
l.insert(3, 99)  # a,b insert b at position a
l.sort()  # sort list
l.sort(reverse=True)  # sort in reverse
print(l)
l.clear()  # clear all elements from the list in PYTHON 3
print(l)

# TUPLE () like list but can't be modified, no append, extend, insert, remove, clear
print("\n\n-------------------------TUPLE-------------------------")
tpl = (10, 20, 30, 10, "xyz")
print(tpl * 3)
print(tpl[3])
print(tpl.count(10))  # count the occurrence of the element in the tuple
print(tpl.index(10))  # gives the index of the element's first occurrence in the tuple
# can use all the functions lke length, max, min like those in list, only those that modify the tuple
lst = [10, 20, 30, 40, 50]
print(tuple(lst))  # convert list to tuple

# SET {} unlike list set doesn't allow duplicate input values, set doesn't have any order
print("\n\n-------------------------SET--------------------------")
s = {10, 10, 20, "xyz"}
s.update([30, 40])  # to add values in the set in any order as set has no order
s.remove(10)  # to remove values from the set
print(s)
# print(s[index], s*3) won't work as set has no order, no duplicate
f = frozenset(s)
# f.update([10]) f.remove(10) won't work on it as being frozen doesn't allow any further changes
print(f)

# RANGE starts from 0 to
r = range(1, 5, 2)  # range(from,to,step)
for i in r:
    print(i)

# BYTES cannot index, remove or add to bytes can do that to BYTEARRAY, no slicing or repetation on either of them
b = bytes(lst)
print(type(b))
b1 = bytearray(lst)
b1[2] = 33

# DICTIONARY {key:value}
print("\n\n---------------------DICTIONARY--------------------")
dict = {1: "a", 2: "b", 3: "c"}
print(dict)  # just print the dictionary as above
print(dict.items())  # gives as the pair seperated in brackets
for i in dict.keys(): print(i)
for i in dict.values(): print(i)
del dict[2]  # deleting the item using key
# clear,del, update, copy, pop ,popitem, setdefault can be done too in dictionary
print(dict)
