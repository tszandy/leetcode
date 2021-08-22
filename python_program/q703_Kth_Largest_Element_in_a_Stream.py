from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        self.nums = self.nums[-self.k:]

    def add(self, val: int) -> int:
        self.nums.insert(bisect_left(self.nums,val),val)
        self.nums = self.nums[-self.k:]
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

sol = Solution()

# input
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

# output
output = sol.KthLargest()
# answer
answer = ""
print(output, answer, answer == output)
