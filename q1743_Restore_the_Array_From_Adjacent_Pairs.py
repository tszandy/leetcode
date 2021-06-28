from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        elem_edge = defaultdict(set)
        for x,y in adjacentPairs:
            elem_edge[x].add(y)
            elem_edge[y].add(x)
            
        return_list = []
        for e in elem_edge:
            if len(elem_edge[e]) ==1:
                first_element = e
                second_element = elem_edge[first_element].pop()
                return_list.append(first_element)
                elem_edge[second_element].remove(first_element)
                break

        while elem_edge[second_element]:
            first_element = second_element
            second_element = elem_edge[first_element].pop()
            return_list.append(first_element)
            elem_edge[second_element].remove(first_element)
        return_list.append(second_element)
        return return_list

sol = Solution()


# input
adjacentPairs = [[2,1],[3,4],[3,2]]
# output
output = sol.restoreArray(adjacentPairs)
# answer
answer = [1,2,3,4]
print(output, answer, answer == output)

# input
adjacentPairs = [[4,-2],[1,4],[-3,1]]
# output
output = sol.restoreArray(adjacentPairs)
# answer
answer = [-2,4,1,-3]
print(output, answer, answer == output)

# input
adjacentPairs = [[100000,-100000]]
# output
output = sol.restoreArray(adjacentPairs)
# answer
answer = [100000,-100000]
print(output, answer, answer == output)
