class MyStack:

    def __init__(self):
        self.res = deque()

    def push(self, x: int) -> None:
        self.res.append(x)
        size = len(self.res)
        for _ in range(size-1):
            tmp = self.res.popleft()
            self.res.append(tmp)
        

    def pop(self) -> int:
        return self.res.popleft()
        

    def top(self) -> int:
        return self.res[0]

    def empty(self) -> bool:
        return len(self.res) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()