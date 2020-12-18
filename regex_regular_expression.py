# Regular expressions also known as REG X are a bunch of characters or a pattern that will create to search
# for a string within a given string or to validate the given string to see if it follows the given pattern


# SEQUENCE CHARACTERS
# to match single character in the string, all sequence character starts with /
# \d - any digit between 0-9
# \D - any non-digit character
# \s - matches the white spaces characters
# \S - matches the non white characters
# \w - for an alpha numeric character any digit or character A-Z
# \W - for non alpha numeric
# \b - spaces around words
# \A - search only at the beginning of string
# \Z -search for character at the end of the string

# QUANTIFIERS
# + after the sequence char specifies one or more after the search expression -- output>=1
# * after the sequence char specifies 0 or more defined search expression -- output>=0
# ? after the sequence char specifies 0 or 1 repetition of the regular expression
# {m} exactly m occurrence of regular expression
# {m,n} min m or max n occurrence of regular expression -- by default m is 0 and n is infinite

# SPECIAL CHARACTER
# \ escape character -  use a backwards slash or any other special characters or within the regular expression
# . dot operator - he dot operator which matches any character except a new line
# ^ power operator - used to match a given regular expression at the beginning of a string
# $ - opposite to ^ - regular expression match happen at the end of the string.
# [..] - specify a range of values within square brackets -- [a-z] all small alphabets from a to z
# [^..] - opposite to [..] -- matches anything not in the bracket
# (..) - matching a regular expression
# (R|S) - matching multiple regular expression either R match or S

# search The search method takes a regular expression and it searches for that format in the given string and it
# returns the very first sub-string within the given string that matches that pattern once the result is returned back.

import re

print("------------------re.search-----------------")
s = "Yo maa boy! One step at a time"
# r'define the regular expression inside here'
r = re.search(r'O\w\w', s)  # --> o\w\w word start with o and has only 2 characters after it
# the search must have the same character which we specify like "O" not "o"
print(r.group())  # .group display the output from re.search
# group method can't work on return as None, can't invoke on None return
# group only for whatever comes from the search method


print("\n\n------------------re.findall-----------------")
# findall
# searches for the pattern from the beginning to the end of the string for all the matched substring
# if nothing matches it return empty list.
s = "Yo maa only boy! One one step at a time"
r = re.findall(r'o\w\w', s)
rq = re.findall(r'o\w+', s) # using quantifiers
rqw = re.findall(r'o\w?', s) # using quantifiers only 0 or 1 character after 'o'
rqwe = re.findall(r'o\w{1,3}', s) # between 1 to 3 character after 'o'
print(r,rq,rqw,rqwe)


print("\n\n------------------re.match-----------------")
# match -- search for the pattern right at the beginning
# if nothing matches it return "none"
r = re.match(r'O\w\w', s)  # none as output
reslt = re.match(r'Y\w', s)  # Yo as output
print(r, reslt, reslt.group())  # no group method used result in giving all details including span, object
# group method removes all that gibberish and return only the matched content


print("\n\n------------------re.split-----------------")
# split
# splits the string into multiple strings using the passed regular expression as a limiter
s = "Yo maa only 1 boy! One one 234 step at a 9 time"
res=re.split(r'\d+',s) # to split across all the digits used as limiter
print(res)


print("\n\n------------------re.sub-----------------")
# substitute
# substitute the specified string with given string
s = "Yo maa only 1 boy! One one 234 step at a 9 time"
res=re.sub(r'one','two',s)  # replace all one's with two
print(res)


print("\n\n------------------dates-----------------")
# finding dates
s = "Yo maa only 1 boy 1-3-2019 ! One one 234 step at a 9 time 11-12-2000"
rqwe = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', s) # between 1 to 3 character after 'o'
print(rqwe)


print("\n\n------------------special character-----------------")
# special character
s = "Yo maa boy! One step at a time"
r = re.search(r'^Y\w*', s)
print(r.group())
