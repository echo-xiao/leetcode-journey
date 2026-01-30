"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""

class Solution:
    def toArray(self, head):
        
        tmp = []
        curr = head
        
        while curr is not None:
            new_element = curr.val
            tmp.append(new_element)
            curr = curr.next
        return tmp