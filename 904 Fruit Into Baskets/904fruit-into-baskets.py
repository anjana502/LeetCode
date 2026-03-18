from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(lambda: 0)
        j = 0
        max1 = 0
        
        for i in range(len(fruits)):
            d[fruits[i]] += 1
            
            while (j < i and len(d) > 2):
                d[fruits[j]] -= 1
                
                if (d[fruits[j]] == 0):
                    del d[fruits[j]]
                
                j += 1
            
            max1 = max(max1, (i - j + 1))
        
        return max1