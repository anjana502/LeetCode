class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.s1 = []
        self.size = maxSize
        self.count = 0

    def push(self, x: int) -> None:
        if (self.count == self.size):
            return
        
        self.s.append(x)
        self.count += 1

    def pop(self) -> int:
        if (self.count == 0):
            return -1
        
        d = self.s.pop()
        self.count -= 1

        return d

    def increment(self, k: int, val: int) -> None:
        while (len(self.s) > k):
            d = self.s.pop()
            self.s1.append(d)
        
        for i in range(len(self.s)):
            self.s[i] += val
        
        while (len(self.s1) != 0):
            d = self.s1.pop()
            self.s.append(d)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)