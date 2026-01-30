class Solution(object):

    def mergeTwoLists(self, list1, list2):
        if list1 is None: return list2
        if list2 is None: return list1

        ptr1 = list1
        ptr2 = list2
        
        if list1.val <= list2.val:
            head = list1
            tail = list1
            ptr1 = ptr1.next
        else:
            head = list2
            tail = list2
            ptr2 = ptr2.next 
    
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                tail = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                tail = ptr2
                ptr2 = ptr2.next
        
        if ptr1 is None:
            tail.next = ptr2
        else:
            tail.next = ptr1
        
        return head
