import math

class Solution:
    def canEat(self, piles, h, mid):
        count = 0

        for i in piles:
            if (i <= mid):
                count += 1
            else:
                q = i // mid
                r = i % mid
                count += q

                if (r > 0):
                    count += 1
        
        if (count <= h):
            return True
        return False
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canEat(piles, h, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result