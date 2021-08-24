from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        self.rows = rows
        self.cols = cols
        self.return_list = []
        self.total_num = rows*cols
        self.step = 1
        self.spiral_order_leftupper_to_rightdown(rStart,cStart,1)
        return self.return_list
        
    def spiral_order_leftupper_to_rightdown(self,x,y,r):
        for i in range(r):
            if self.step>self.total_num:
                return
            if 0<=x<self.rows and 0<=y<self.cols:
                self.return_list.append([x,y])
                self.step+=1

            y+=1
        for i in range(r):
            if self.step>self.total_num:
                return
            if 0<=x<self.rows and 0<=y<self.cols:
                self.return_list.append([x,y])
                self.step+=1
            x+=1
        
        self.spiral_order_rightdown_to_leftupper(x,y,r+1)

    def spiral_order_rightdown_to_leftupper(self,x,y,r):
        for i in range(r):
            if self.step>self.total_num:
                return
            if 0<=x<self.rows and 0<=y<self.cols:
                self.return_list.append([x,y])
                self.step+=1

            y-=1
        for i in range(r):
            if self.step>self.total_num:
                return
            if 0<=x<self.rows and 0<=y<self.cols:
                self.return_list.append([x,y])
                self.step+=1
            x-=1

        self.spiral_order_leftupper_to_rightdown(x,y,r+1)


sol = Solution()

# input
rows = 1

cols = 4

rStart = 0

cStart = 0

# output
output = sol.spiralMatrixIII(rows,cols,rStart,cStart)
# answer
answer = [[0,0],[0,1],[0,2],[0,3]]

print(output, answer, answer == output)

# input
rows = 5

cols = 6

rStart = 1

cStart = 4

# output
output = sol.spiralMatrixIII(rows,cols,rStart,cStart)
# answer
answer = [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

print(output, answer, answer == output)
