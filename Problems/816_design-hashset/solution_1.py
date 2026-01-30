class MyHashSet(object):

    def __init__(self):
        self.capacity = 10000
        self.buckets = [ListNode(0) for _ in range(self.capacity)]


    def add(self, key):
        index = key % self.capacity
        head = self.buckets[index]
        
        curr = head.next
        while curr is not None:
            if curr.val == key:
                return 
            curr = curr.next
        
        new = ListNode(key)
        new.next = head.next
        head.next = new

        

    def remove(self, key):
        index = key % self.capacity
        head = self.buckets[index]

        prev = head
        curr = head.next
        while prev is not None and curr is not None:
            if curr.val == key:
                prev.next = curr.next
                return
            else:
                curr = curr.next
                prev = prev.next
        return

        

        

    def contains(self, key):
        index = key % self.capacity
        head = self.buckets[index]

        curr = head.next
        while curr is not None:
            if curr.val == key:
                return True
            else:
                curr = curr.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)