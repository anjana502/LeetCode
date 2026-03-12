class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = [0 for i in range(len(chalk))]
        prefix_sum[0] = chalk[0]

        for i in range(1, len(chalk)):
            prefix_sum[i] = chalk[i] + prefix_sum[i - 1]

        index = 0
        k %= prefix_sum[-1]

        while (chalk[index] <= k):
            low = 0
            high = len(chalk) - 1

            while (low <= high):
                mid = low + (high - low) // 2

                if (prefix_sum[mid] <= k):
                    index = mid
                    low = mid + 1
                else:
                    high = mid - 1

            k -= prefix_sum[index]
            index = (index + 1) if (index != len(chalk) - 1) else 0

        return index               