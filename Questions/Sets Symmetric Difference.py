'''Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12

#############################################################################################################'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
inp=input().split(" ")
array_m=list()
for i in inp:
    array_m.append(int(i))
n=int(input())
inp=input().split(" ")
array_n=list()
for i in inp:
    array_n.append(int(i))
set_m=set(array_m)
set_n=set(array_n)
diff_set=set()
diff_set.update(set_m.difference(set_n))
diff_set.update(set_n.difference(set_m))
for i in sorted(diff_set):
    print(i)

    
