# arthemetic operators
print("-------------------ARITHMETIC OPERATOR------------------")
a, b = 5, 10
print(a + b, a * b, a - b, a / b, a % b, a ** b, a // b)
# a+b addition
# a-b subtraction
# a*b multiplication
# a/b division
# a%b modulus
# a**b a^b a power b
# a//b floor value of division


# assignment operator
print("\n\n-------------------ASSIGNMENT OPERATOR------------------")
a += b  # a=a+b
print(a)
a *= b  # a=a*b
print(a)

# comparision operator
print("\n\n-------------------COMPARISION OPERATOR------------------")
print(a == b)  # ii a = b or not
print(a != b)  # is a =/= b or not
print(a > b)  # is a>b or not
print(a < b)  # is a<b or not
print(a <= b)  # is a<=b or not
print(a >= b)  # is a>=b or not

# logical operators --booleans
print("\n\n-------------------LOGICAL OPERATOR------------------")
x = 20
y = 30
print(x == 25 and y == 30)
print(x == 25 or y == 30)
print(not (x == 25 and y == 30))
print(not (x == 25 or y == 30))
