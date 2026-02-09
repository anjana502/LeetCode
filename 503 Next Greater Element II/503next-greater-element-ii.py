class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ls = [-1 for i in range(len(nums))]

        for i in range(len(nums)):
            curr = nums[i]

            while (len(stack) != 0 and nums[stack[-1]] < curr):
                index = stack.pop()
                ls[index] = curr
            
            stack.append(i)
        
        for i in range(len(nums)):
            curr = nums[i]

            while (len(stack) != 0 and nums[stack[-1]] < curr):
                index = stack.pop()
                ls[index] = curr
            
            stack.append(i)
        
        return ls