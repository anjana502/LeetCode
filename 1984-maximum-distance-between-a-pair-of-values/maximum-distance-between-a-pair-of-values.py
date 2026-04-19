class Solution:
    def binarySearch(self, nums, target, low, high):
        index = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (nums[mid] >= target):
                index = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return index
    
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max1 = 0
        n = len(nums2)

        for i in range(len(nums1)):
            index = self.binarySearch(nums2, nums1[i], i, n - 1)

            if (index != -1):
                max1 = max(max1, (index - i))
        
        return max1