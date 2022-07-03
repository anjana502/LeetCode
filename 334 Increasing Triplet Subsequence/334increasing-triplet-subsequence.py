class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ls1 = [0 for i in range(len(nums))]
        s = []
        s.append(nums[-1])
        ls1[-1] = None
        for i in range(len(nums) - 2, -1, -1):
            p = nums[i]
            while (len(s) != 0 and s[-1] <= p):
                s.pop()
            if (len(s) != 0):
                ls1[i] = s[-1]
            else:
                ls1[i] = None
            s.append(p)
        
        ls2 = [0 for i in range(len(nums))]
        s = []
        s.append(nums[0])
        ls2[0] = None
        for i in range(1, len(nums)):
            p = nums[i]
            while (len(s) != 0 and s[-1] >= p):
                s.pop()
            if (len(s) != 0):
                ls2[i] = s[-1]
            else:
                ls2[i] = None
            s.append(p)
        
        for i in range(len(nums)):
            if (ls1[i] != None and ls2[i] != None):
                print((ls1[i], ls2[i]))
                if (nums[i] > ls2[i] and nums[i] < ls1[i]):
                    return True
        return False
        
        
        