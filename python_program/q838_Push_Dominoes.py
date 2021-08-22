from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        to_right_list = [0]*n
        to_left_list = [0]*n
        
        count = 0
        right_signal = False
        for i in range(n):
            if dominoes[i]=="R":
                count = 1
                to_right_list[i] = count
                right_signal = True
            if dominoes[i]=="L":
                to_right_list[i]=0
                right_signal = False
            if dominoes[i]=="." and right_signal:
                count += 1
                to_right_list[i] = count
        del right_signal
                
        count = 0
        left_signal = False
        for i in range(n)[::-1]:
            if dominoes[i]=="L":
                count = 1
                to_left_list[i] = count
                left_signal = True
            if dominoes[i]=="R":
                to_left_list[i]=0
                left_signal = False
            if dominoes[i]=="." and left_signal:
                count += 1
                to_left_list[i] = count
        
        result = ["."]*n
        for i in range(n):
            if to_left_list[i] == to_right_list[i]:
                result[i] = "."
                continue
            if to_left_list[i] == 0:
                result[i] = "R"
                continue
            if to_right_list[i] == 0:
                result[i] = "L"
                continue
            if to_left_list[i] < to_right_list[i]:
                result[i] = "L"
                continue
            if to_left_list[i] > to_right_list[i]:
                result[i] = "R"
                continue
        return "".join(result)

sol = Solution()


# input
dominoes = ".L.R...LR..L.."
# output
output = sol.pushDominoes(dominoes)
# answer
answer = "LL.RR.LLRRLL.."
print(output, answer, answer == output)

# input
dominoes = "RR.L"
# output
output = sol.pushDominoes(dominoes)
# answer
answer = "RR.L"
print(output, answer, answer == output)

# input
dominoes = ".L.R...LR..L...L.R...LR..L...R...LR..L.....LR..L...L.R...LR..L.."
# output
output = sol.pushDominoes(dominoes)
# answer
answer = "LL.RR.LLRRLLLLLL.RR.LLRRLL...RR.LLRRLLLLLLLLRRLLLLLL.RR.LLRRLL.."
print(output, answer, answer == output)
