from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        self.a = self.b = 1
        while not(self.a<=label <=self.b):
            self.a=2*self.a
            self.b=2*self.b+1
        self.return_list = []
        self.path_in_zig_zag_tree(label)
        return self.return_list[::-1]
        
    def path_in_zig_zag_tree(self,label):
        if label == 1:
            self.return_list.append(1)
            return
        self.return_list.append(label)        
        self.a//=2
        self.b//=2
        self.path_in_zig_zag_tree(self.a+self.b-label//2)

sol = Solution()

# input
label = 1

# output
output = sol.pathInZigZagTree(label)
# answer
answer = [1]
print(output, answer, answer == output)

# input
label = 14

# output
output = sol.pathInZigZagTree(label)
# answer
answer = [1,3,4,14]
print(output, answer, answer == output)

# input
label = 26

# output
output = sol.pathInZigZagTree(label)
# answer
answer = [1,2,6,10,26]
print(output, answer, answer == output)

# input
label = 248

# output
output = sol.pathInZigZagTree(label)
# answer
answer = [1,3,4,15,16,62,67,248]
print(output, answer, answer == output)

# input
label = 8593

# output
output = sol.pathInZigZagTree(label)
# answer
answer = [1,2,7,8,31,33,124,134,499,537,1997,2148,7991,8593]
print(output, answer, answer == output)

# input
label = 328949

# output
output = sol.pathInZigZagTree(label)
# answer
answer = [1,3,5,13,20,55,80,223,321,893,1284,3574,5139,14296,20559,57185,82237,228741,328949]
print(output, answer, answer == output)
