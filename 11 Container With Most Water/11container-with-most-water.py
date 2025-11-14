class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max1 = 0

        while (left < right):
            d = min(height[left], height[right]) * (right - left)
            max1 = max(max1, d)

            if (height[left] <= height[right]):
                left += 1
            else:
                right -= 1
        
        return max1