from collections import deque

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        q_pos = deque()
        q_neg = deque()
        n = len(nums)
        ls = [0 for i in range(n)]

        for i in range(n):
            if (nums[i] > 0):
                q_pos.append(nums[i])
            else:
                q_neg.append(nums[i])
        
        for i in range(n):
            if (i % 2 == 0):
                ls[i] = q_pos.popleft()
            else:
                ls[i] = q_neg.popleft()
        
        return ls