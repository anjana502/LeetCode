class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if (len(self.stack) == 0):
            self.stack.append((price, 1))

            return 1
        
        count = 1

        while (len(self.stack) != 0 and price >= self.stack[-1][0]):
            p, d = self.stack.pop()
            count += d
        
        self.stack.append((price, count))

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)