from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict(lambda: 0)

        for i in arr:
            d[i % k] += 1
        
        if (d[0] % 2 != 0):
            return False
        
        for i in range(1, k // 2 + 1):
            if (d[i] != d[k - i]):
                return False
        
        return True