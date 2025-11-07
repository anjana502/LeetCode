class Solution:
    def merge(self, nums, low, mid, high):
        n1 = mid - low + 1
        n2 = high - mid
        left = [nums[low + i] for i in range(n1)]
        right = [nums[mid + 1 + j] for j in range(n2)]
        i = 0
        j = 0
        k = low

        while (i < n1 and j < n2):
            if (left[i] <= right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while (i < n1):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while (j < n2):
            nums[k] = right[j]
            j += 1
            k += 1
        
    def mergeSort(self, nums, low, high):
        if (low < high):
            mid = low + (high - low) // 2
            self.mergeSort(nums, low, mid)
            self.mergeSort(nums, mid + 1, high)
            self.merge(nums, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)

        return nums