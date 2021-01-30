# ALL DATATYPES IN PYTHON ARE OBJECT TYPES AND HAVE A ASSOCIATED CLASS

# assigning datatypes and value
a = 13
b = 100
c = 66
print(a, b, c)  # simple

x = 33.5
y = 205  # int untill u add .0 at end else python take it as int
z = 205.0  # float
print(x, y, z)
print(type(x), type(y), type(z))  # type of dataset

d = 1 + 5j  # complex
print(d, type(d))

e = 0B1011  # binary start with "0B"
f = 0XFF  # hexa start with "0X"
g = 0O33  # oct start with "0O"
print(e, f, g)

h = True  # boolean True and False
print(type(g), 9 < 8)

i = int(x)  # converting into different datatypes
j = float(a)  # conveting int to float
k = bin(c)  # converting into different base "bin,oct,hex"
print(i, type(i), j, type(j), k, type(k))

s = "hey there"
s1 = """hey
there"""
print(s)
print(s1)

s = "  hey there  "
print(s[1])  # access location in the string
print(s * 3)  # print string multiple time
print(len(s))  # length of string

print(s[0:5])  # slicing
print(s[0:])
print(s[:4])
print(s[-3:-1])  # -1 is the last character
print(s[0:8:2])  # slicing with step jump
print(s[::-1])  # to reverse string
print(s[9::-1])  # to reverse the string
print(s.strip(), s.lstrip(), s.rstrip())

print(s.find("er", 0, len(s)))  # find a string "s.find("looking for",search_start_index,search_end_indes)"
# if not found it give -1 as output

print(s.count("e"))  # occurence of charater number of times

print(s.replace("hey", "hello"))  # replacing string parts "s.replace("old","new")"

print(s.upper(), s.lower(), s.title())  # all upper case, all lower case, all first character uppercase


# in case we wanna captialize only the first alphabatical letter-- abc -> Abc but 12abc -> 12abc stays
s=input()
for i in s[:].split():
        s=s.replace(i,i.capitalize())
    return s
