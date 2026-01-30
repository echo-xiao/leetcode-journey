class MyStack:

    def __init__(self):
        self.res = deque()

    def push(self, x: int) -> None:
        self.res.append(x)
        for _ in range(0, len(self.res)-1):
            tmp = self.res.popleft()
            self.res.append(tmp)

    def pop(self) -> int:
        return self.res.popleft()

    def top(self) -> int:
        return self.res[0]

    def empty(self) -> bool:
        if len(self.res) == 0:
            return True
        else:
            return False

