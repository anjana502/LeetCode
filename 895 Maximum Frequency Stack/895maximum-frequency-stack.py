from collections import defaultdict
import heapq

class FreqStack:

    def __init__(self):
        self.q = []
        heapq.heapify(self.q)
        self.d = defaultdict(lambda: 0)
        self.top = 0

    def push(self, val: int) -> None:
        self.d[val] += 1
        self.top += 1
        heapq.heappush(self.q, (-1 * self.d[val], -1 * self.top, val))

    def pop(self) -> int:
        count, t, val = heapq.heappop(self.q)
        self.d[val] -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()