from collections import defaultdict
from functools import reduce
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = defaultdict(lambda: 0)
        
        for i in deck:
            d[i] += 1
        
        result = reduce(gcd, d.values())
        
        if (result >= 2):
            return True
        return False