# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def maxDepth(self, nestedList, d):
        max1 = d
        
        for i in nestedList:
            if (i.isInteger() == False):
                max1 = max(max1, self.maxDepth(i.getList(), d + 1))
        
        return max1
    
    def depthSumInverse1(self, nestedList, max1, d):
        sum1 = 0
        
        for i in nestedList:
            if (i.isInteger() == True):
                sum1 += ((max1 - d + 1) * i.getInteger())
            else:
                sum1 += self.depthSumInverse1(i.getList(), max1, d + 1)
        
        return sum1
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max1 = self.maxDepth(nestedList, 1)
        
        sum1 = self.depthSumInverse1(nestedList, max1, 1)
        
        return sum1
        