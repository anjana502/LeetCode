import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []
        heapq.heapify(q)
        q.append((nums1[0] + nums2[0], 0, 0))
        count = 0
        ls = []
        s = set()
        s.add((0, 0))

        while (len(q) != 0 and count < k):
            sum1, i, j = heapq.heappop(q)
            ls.append([nums1[i], nums2[j]])

            if (i + 1 < len(nums1) and ((i + 1, j) not in s)):
                heapq.heappush(q, (nums1[i + 1] + nums2[j], i + 1, j))
                s.add((i + 1, j))
            if (j + 1 < len(nums2) and ((i, j + 1) not in s)):
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
                s.add((i, j + 1))
            
            count += 1
        
        return ls