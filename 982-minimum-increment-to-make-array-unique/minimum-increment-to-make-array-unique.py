from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)

        for i in nums:
            d[i] += 1
        
        d = dict(sorted(d.items()))
        
        s = set(nums)
        curr = min(d.keys())
        count = 0

        for i in d:
            while (d[i] > 1):
                if (curr < i):
                    curr = i + 1
                
                while (curr in s):
                    curr += 1
                
                count += (curr - i)
                s.add(curr)
                d[i] -= 1

        return count