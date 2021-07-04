from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = np.array(rectangle)
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.rectangle[row1:row2+1,col1:col2+1] = newValue
        

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row,col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

sol = SubrectangleQueries()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
