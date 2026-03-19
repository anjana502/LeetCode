from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()

    def next(self, val: int) -> float:
        self.q.append(val)
        
        if (len(self.q) > self.size):
            self.q.popleft()
        
        avg = sum(self.q) / len(self.q)
        
        return avg

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)