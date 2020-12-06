# if else elif transfer while for break continue pass return
# if condition : statment else condition: statment
i = int(input("enter a number: "))
if i > 0:
    print("1+")
elif i == 0:
    print("zero")
else:
    print("1-")

# while condition: statment
j = 0
while j < i:
    print(j)
    j += 1  # no x++ in python

# for var in sequence: statment
for j in range(5):
    print(j)
l = [1, 2, 3, 4, 5]
p = 1
for i in range(len(l)):
    p = p * l[i]
print(p)

# break breaks out of loop not if condition
for i in range(10):
    if i == 8:
        break
    elif i % 3 == 0:
        continue
    print(i)

# assert
x = int(input("enter number: "))
assert x > 10, "wrong number"
print("u entered ", x)
