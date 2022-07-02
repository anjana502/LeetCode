class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1 = {}
        for i in nums1:
            for j in nums2:
                sum1 = i + j
                if (sum1 in d1):
                    d1[sum1] += 1
                else:
                    d1[sum1] = 1
        
        d2 = {}
        for i in nums3:
            for j in nums4:
                sum1 = i + j
                if (sum1 in d2):
                    d2[sum1] += 1
                else:
                    d2[sum1] = 1
        
        count = 0
        for i in d1:
            if (-i in d2):
                count += d1[i] * d2[-i]
        return count