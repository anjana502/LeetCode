class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        flag = True
        
        for i in range(1, len(nums)):
            if (flag == True and nums[i] < nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            elif (flag == False and nums[i] > nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            
            flag = not flag