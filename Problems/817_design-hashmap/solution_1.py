class ListNode(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap(object):

    def __init__(self):
        self.capacity = 10000
        self.buckets = [ListNode() for _ in range(self.capacity)]

    def put(self, key, value):
        index = key % self.capacity
        head = self.buckets[index]

        curr = head.next
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next 
        
        new = ListNode(key,value)
        new.next = head.next
        head.next = new
        

    def get(self, key):
        index = key % self.capacity
        head = self.buckets[index]

        curr = head.next
        while curr is not None:
            if curr.key == key:
                return curr.value
            else:
                curr = curr.next
        return -1
        

        

    def remove(self, key):
        index = key % self.capacity
        head = self.buckets[index]

        prev = head
        curr = head.next
        while prev is not None and curr is not None:
            if curr.key == key:
                prev.next = curr.next
                curr = curr.next
                return
            else:
                prev = prev.next
                curr = curr.next
            



        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)