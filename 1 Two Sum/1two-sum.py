class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        index = {}

        for i in range(len(nums)):
            if (nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            
            index[nums[i]] = i
        
        for i in range(len(nums)):
            sum1 = target - nums[i]

            if (sum1 in d):
                if ((sum1 == nums[i] and d[nums[i]] > 1) or (sum1 != nums[i])):
                    ls = [i, index[sum1]]
                    return ls