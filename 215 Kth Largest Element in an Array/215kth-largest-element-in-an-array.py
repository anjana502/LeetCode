import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        heapq.heapify(q)

        for i in nums:
            heapq.heappush(q, i)

            if (len(q) > k):
                heapq.heappop(q)
        
        d = heapq.heappop(q)

        return d