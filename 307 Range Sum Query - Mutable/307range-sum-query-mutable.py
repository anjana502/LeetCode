class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.ls = [0 for i in range(n + 1)]
    
    def update(self, x, d):
        while (x <= self.n):
            self.ls[x] += d
            x += (x & -x)
    
    def query(self, x):
        sum1 = 0
        
        while (x > 0):
            sum1 += self.ls[x]
            x -= (x & -x)
        
        return sum1

class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = BinaryIndexedTree(len(nums))
        
        for i in range(len(nums)):
            self.tree.update(i + 1, nums[i])

    def update(self, index: int, val: int) -> None:
        curr_val = self.sumRange(index, index)
        d = val - curr_val
        
        self.tree.update(index + 1, d)

    def sumRange(self, left: int, right: int) -> int:
        sum1 = self.tree.query(right + 1) - self.tree.query(left)
        
        return sum1


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)