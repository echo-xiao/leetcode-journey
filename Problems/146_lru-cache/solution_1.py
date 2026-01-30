class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove_node(node)
        self.add_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.dic:
            node = self.dic[key]
            node.value = value
            
            self.remove_node(node)
            self.add_to_head(node)
        else:
            node = Node(key, value)
            self.dic[key] = node
            self.add_to_head(node)

            if len(self.dic) > self.capacity:
                lru_node = self.tail.prev
                self.remove_node(lru_node)
                del self.dic[lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)