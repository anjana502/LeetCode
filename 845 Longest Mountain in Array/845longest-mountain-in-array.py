class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left = [0 for i in range(len(arr))]
        right = [0 for i in range(len(arr))]

        for i in range(1, len(arr)):
            if (arr[i] > arr[i - 1]):
                left[i] = left[i - 1] + 1
        
        for j in range(len(arr) - 2, -1, -1):
            if (arr[j] > arr[j + 1]):
                right[j] = right[j + 1] + 1
        
        max1 = 0

        for i in range(1, len(arr) - 1):
            if (left[i] != 0 and right[i] != 0):
                d = left[i] + right[i] + 1
                max1 = max(max1, d)
        
        return max1