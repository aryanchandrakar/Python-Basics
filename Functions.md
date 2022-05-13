## STRINGS

1. `upper()` - change string to upper case 
2. `lower()` - change string to lower case
3. `split("-")` - breaks string into array, dividing where the char given in () is found
4. `"-".join(array)` - join the array of strings to form a line with char in "" used to join them
5. `list(s)` - converts string s into list of char
6. `str.isalnum()` - checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9); 'ab123'.isalnum() -> True
7. `str.isalpha()` - checks if all the characters of a string are alphabetical (a-z and A-Z); 'abcd**1**'.isalpha() -> False
8. `str.isdigit()` - checks if all the characters of a string are digits (0-9); '1234'.isdigit() -> True
9. `str.islower()` - checks if all the characters of a string are lowercase characters (a-z); 'abcd123#'.islower() -> True
10. `str.isupper()` - checks if all the characters of a string are uppercase characters (A-Z); 'ABCD123#'.isupper() -> True
11. `str.ljust(width)` - This method returns a left aligned string of length width; 'abcdefghij'.ljust(20,'-') -> abcdefghij----------  
12. `str.center(width)` - returns a centered string of length width; 'abcdefghij'.center(20,'-') -> -----abcdefghij-----
13. `str.rjust(width)` - returns a right aligned string of length width; 'abcdefghij'.rjust(20,'-') -> ----------abcdefghij
14.  `textwrap.wrap(text, width=70, **kwargs)` - This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content. Default width is taken as 70.
15.  `textwrap.fill(text, width=70, **kwargs)` - The fill() convenience function works similar to textwrap.wrap except it returns the data joined into a single, newline-separated string. This function wraps the input single paragraph in text, and returns a single string containing the wrapped paragraph.
16. `textwrap.dedent(text)` - This function is used to remove any common leading whitespace from every line in the input text. This allows to use docstrings or embedded multi-line strings line up with the left edge of the display, while removing the formatting of the code itself.
17. `textwrap.shorten(text, width, **kwargs)` - This function truncates the input string so that the length of the string becomes equal to the given width. At first, all the whitespaces are collapsed in the string by removing the whitespaces with a single space. If the modified string fits in the given string, then it is returned otherwise, the characters from the end are dropped so that the remaining words plus the placeholder fit within width.
18. `textwrap.indent(text, prefix, predicate=None)` - This function is used to add the given prefix to the beginning of the selected lines of the text. The predicate argument can be used to control which lines are indented.
