# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        fast = slow.next
        slow.next = None

        lst1 = head
        lst2 = self.reverse(fast)

        self.merge(lst1, lst2)

    def merge(self, lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        
        while lst1 is not None and lst2 is not None:
            tmp1 = lst1.next
            tmp2 = lst2.next

            lst1.next = lst2
            lst2.next = tmp1

            lst2 = tmp2
            lst1 = tmp1

        return lst1


    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp
        
        return prev
        