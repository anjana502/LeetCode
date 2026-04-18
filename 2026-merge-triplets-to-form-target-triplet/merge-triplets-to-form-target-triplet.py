class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        max1 = 0
        max2 = 0
        max3 = 0

        for i, j, k in triplets:
            if ((i <= x) and (j <= y) and (k <= z)):
                max1 = max(max1, i)
                max2 = max(max2, j)
                max3 = max(max3, k)
        
        if ([max1, max2, max3] == target):
            return True
        return False