# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        leftDummy = ListNode(0)
        middleDummy = ListNode(0)
        rightDummy = ListNode(0)

        leftTail = leftDummy
        middleTail = middleDummy
        rightTail = rightDummy

        cnt = 1
        curr = head 
        while curr is not None:
            tmp = curr.next
            curr.next = None
            if cnt < left:
                leftTail.next = curr
                leftTail = leftTail.next
            elif cnt >= left and cnt <= right:
                middleTail.next = curr
                middleTail = middleTail.next
            else:
                rightTail.next = curr
                rightTail = rightTail.next
            cnt += 1
            curr = tmp

        newMidHead = self.reversed(middleDummy.next)
        leftTail.next = newMidHead

        if middleDummy.next is not None:
            middleDummy.next.next = rightDummy.next
        else:
            leftTail.next = rightDummy.next

        return leftDummy.next

    def reversed(self, node: Optional[ListNode]) -> Optional[ListNode]:

        curr = node
        prev = None

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        return prev

                
                