"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        addition=ListNode()
        
        add=addition
        while (l1 and l2):
            a=l1.val+l2.val+carry
            tens=math.floor(a/10)
            ones=a-tens*10
            carry=tens
            Node=ListNode()
            Node.val=int(ones)
            add.next=Node
            l1=l1.next
            l2=l2.next
            add=add.next
        if (l1):
            while l1:
                a=l1.val+carry
                tens=math.floor(a/10)
                ones=a-tens*10
                carry=tens
                Node=ListNode()
                Node.val=int(ones)
                add.next=Node
                l1=l1.next
                add=add.next
        if (l2):
            while l2:
                a=l2.val+carry
                tens=math.floor(a/10)
                ones=a-tens*10
                carry=tens
                Node=ListNode()
                Node.val=int(ones)
                add.next=Node
                l2=l2.next
                add=add.next
        if carry!=0:
            Node=ListNode()
            Node.val=int(carry)
            add.next=Node
        addition=addition.next
        return(addition)
