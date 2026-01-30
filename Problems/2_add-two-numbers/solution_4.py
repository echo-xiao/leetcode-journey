# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans1 = self.transform(l1)
        ans2 = self.transform(l2)
        nums = ans1 + ans2
        nums = str(nums)
        
        dummy = ListNode(0)
        curr = dummy
        for num in reversed(nums):
            curr.next = ListNode(int(num))
            curr = curr.next

        return dummy.next

    def transform(self, node: Optional[ListNode]) -> int:

        curr = node
        res = []
        while curr is not None:
            res.append(curr.val)
            curr = curr.next

        res.reverse()

        if not res:
            return 0

        ans = "".join(map(str, res))
        return int(ans)
        
