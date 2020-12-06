import sys

# import sys library to use arguments
accbal = 10000
l = sys.argv
# arguments saved in list in string format

print("[1] check balance")
print("[2] withdraw")
print("[3] deposit cash")
print("[4] deposit check")
a = int(l[1])
if a == 1:
    print("balance: ", accbal)
elif a == 2:
    # b accessed here cause if case 1 was chosen bo l[2] would be there cause index error
    b = int(l[2])
    accbal = accbal - b
    print("balance: ", accbal)
elif a == 3:
    b = int(l[2])
    accbal = accbal + b
    print("balance: ", accbal)
elif a == 4:
    b = int(l[2])
    accbal = accbal + b
    print("balance: ", accbal)
else:
    print("[-] error")
