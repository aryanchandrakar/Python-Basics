# list=[expression for item in iterable if condition]
# shortcut of creating one list out of another while applying a condition to it
lst = [x for x in input("enter 3 numbers seperated by comma:").split(',')] # split uses space by default storing it in x
print(lst) # giving it as output in "'" cause now the input is recorded in string type
# we can typecast it to integer
lst = [int(x) for x in input("enter 3 numbers seperated by comma:").split(',')] # split uses space by default storing it in x
print(lst) # giving it as output in "'" cause now the input is recorded in string type

# if condition in list comprehension
print("\n\n-------if condition in list comprehension-------")
lst = [x for x in range(1,21) if x%2==0] # split uses space by default storing it in x
print(lst) # giving it as output in "'" cause now the input is recorded in string type
print("[-] using range")
# same using jump in range
lst = [x for x in range(1,21,2) ] # split uses space by default storing it in x
print(lst) # giving it as output in "'" cause now the input is recorded in string type


# products of list
print("\n\n------------product of list-----------")
a=[1,2,3,4,5]
b=[2,3,4,5,6]

# the usual
z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)

# lift the notch use list!
z=[a[i]*b[i] for i in range(len(a)) ]
print(z)


# find the doppelganger
print("\n\n-----------find the doppelganger------------")
r=[]
for i in a:
    if i in b:
        r.append(i)
print(r)

# using list comp
r=[i for i in a if i in b]
print(r)

