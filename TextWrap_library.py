'''
1. textwrap.wrap(text, width=70, **kwargs): This function wraps the input paragraph such that each line in the paragraph is at most width characters long. The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content. Default width is taken as 70.
2. textwrap.fill(text, width=70, **kwargs): The fill() convenience function works similar to textwrap.wrap except it returns the data joined into a single, newline-separated string. This function wraps the input single paragraph in text, and returns a single string containing the wrapped paragraph.
3. textwrap.dedent(text): This function is used to remove any common leading whitespace from every line in the input text. This allows to use docstrings or embedded multi-line strings line up with the left edge of the display, while removing the formatting of the code itself.
4. textwrap.shorten(text, width, **kwargs): This function truncates the input string so that the length of the string becomes equal to the given width. At first, all the whitespaces are collapsed in the string by removing the whitespaces with a single space. If the modified string fits in the given string, then it is returned otherwise, the characters from the end are dropped so that the remaining words plus the placeholder fit within width.
5. textwrap.indent(text, prefix, predicate=None): This function is used to add the given prefix to the beginning of the selected lines of the text. The predicate argument can be used to control which lines are indented.

################################ import textwrap #################################

You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(width=4)
    strlis =(textwrap.wrap(string, max_width))
    return ("\n".join(strlis))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
