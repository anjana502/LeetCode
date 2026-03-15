class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = float("inf")
        p = 0

        for i in prices:
            min1 = min(min1, i)
            p = max(p, i - min1)
        
        return p