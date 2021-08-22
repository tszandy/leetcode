from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.store_list = []
        while nestedList:
            elem = nestedList.pop()
            if not elem.isInteger():
                for e in elem.getList():
                    nestedList.append(e)
            else:
                self.store_list.append(elem)
        self.store_list = self.store_list[::-1]
        self.n = len(self.store_list)
        self.index = 0
        
    def next(self) -> int:
        result = self.store_list[self.index]
        self.index+=1
        return result
    
    def hasNext(self) -> bool:
        return self.index<self.n

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

sol = Solution()

# input
[[1,1],2,[1,1]]
[1,[4,[6]]]
# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
