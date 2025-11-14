class MinStack:

    def __init__(self):
        self.stack = []
        self.min1 = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min1 = min(self.min1, val)

    def pop(self) -> None:
        d = self.stack.pop()

        if (d == self.min1):
            if (len(self.stack) == 0):
                self.min1 = float("inf")
            else:
                self.min1 = min(self.stack)        

    def top(self) -> int:
        return (self.stack[-1])

    def getMin(self) -> int:
        return (self.min1)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()