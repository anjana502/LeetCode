class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        index = -1
        
        while (low <= high):
            mid = low + (high - low) // 2
            
            if (nums[mid] == target):
                index = mid
                high = mid - 1
            elif (nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        
        ls = [-1, -1]
        
        if (index == -1):
            return ls
        
        ls[0] = index
        j = index
        
        while (j < len(nums) and nums[j] == nums[index]):
            j += 1
        
        ls[1] = j - 1
        
        return ls