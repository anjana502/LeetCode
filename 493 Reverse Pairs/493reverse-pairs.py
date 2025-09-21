class Solution:
    def merge(self, nums, low, mid, high):
        j = mid + 1
        count = 0

        for i in range(low, mid + 1):
            while ((j <= high) and (nums[i] > 2 * nums[j])):
                j += 1
            
            count += (j - mid - 1)

        n1 = mid - low + 1
        n2 = high - mid
        left = [nums[low + i] for i in range(n1)]
        right = [nums[mid + 1 + i] for i in range(n2)]
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
        
        return count
        
    def mergeSort(self, nums, low, high):
        count = 0

        if (low < high):
            mid = low + (high - low) // 2

            count += self.mergeSort(nums, low, mid)
            count += self.mergeSort(nums, mid + 1, high)
            count += self.merge(nums, low, mid, high)
        
        return count

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)