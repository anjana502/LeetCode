class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max1 = 0
        n = len(arr)
        sign = 0
        d = 0

        for i in range(n - 1):
            if (arr[i] > arr[i + 1]):
                d = (d + 1) if (sign == -1) else 1
                sign = 1
            elif (arr[i] < arr[i + 1]):
                d = (d + 1) if (sign == 1) else 1
                sign = -1
            else:
                d = 0
                sign = 0
            
            max1 = max(max1, d)
        
        return (max1 + 1)