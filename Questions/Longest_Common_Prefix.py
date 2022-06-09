"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs)==1):
            return strs[0]
        
        minlen=len(strs[0])
        for i in strs:
            if(len(i)<minlen):
                minlen=len(i)
        
        
        comm=""
        for j in range(1,minlen+1):
            commpre=strs[0][0:j]
            
            flag=False
            for i in range(1,len(strs)):
                if (strs[i][0:j] == commpre):
                    flag=True
                else:
                    flag=False
                    break
            if flag==True:
                comm=commpre
        return comm
                
            
