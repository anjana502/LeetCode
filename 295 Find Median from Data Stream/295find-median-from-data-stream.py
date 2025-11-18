import heapq

class MedianFinder:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        heapq.heapify(self.q1)
        heapq.heapify(self.q2)

    def addNum(self, num: int) -> None:
        if ((len(self.q1) == 0) or (num <= -1 * self.q1[0])):
            heapq.heappush(self.q1, -1 * num)
        else:
            heapq.heappush(self.q2, num)
        
        if (abs(len(self.q1) - len(self.q2)) > 1):
            if (len(self.q1) > len(self.q2)):
                d = -1 * heapq.heappop(self.q1)
                heapq.heappush(self.q2, d)
            else:
                d = heapq.heappop(self.q2)
                heapq.heappush(self.q1, -1 * d)

    def findMedian(self) -> float:
        if (len(self.q1) == len(self.q2)):
            return ((-1 * self.q1[0] + self.q2[0]) / 2)
        elif (len(self.q1) > len(self.q2)):
            return (-1 * self.q1[0])
        else:
            return (self.q2[0]) 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()