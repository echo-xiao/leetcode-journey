class MyStack:

    def __init__(self):
        res = []
        self.res = res

    def push(self, x: int) -> None:
        self.res.append(x)
        
        

    def pop(self) -> int:
        return self.res.pop()
        

    def top(self) -> int:
        return self.res[-1]

    def empty(self) -> bool:
        if len(self.res) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()