from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtracking(S,left,right):
            if len(S) == 2*n:
                result.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtracking(S,left+1,right)
                S.pop()
            if right < left:
                S.append(")")
                backtracking(S,left,right+1)
                S.pop()
        backtracking([],0,0)
        return result

sol = Solution()


# input
n = 1
# output
output = sol.generateParenthesis(n)
# answer
answer = ["()"]
print(output, answer, sorted(answer) == sorted(output))

# input
n = 2
# output
output = sol.generateParenthesis(n)
# answer
answer = ["()()","(())"]
print(output, answer, sorted(answer) == sorted(output))

# input
n = 3
# output
output = sol.generateParenthesis(n)
# answer
answer = ["((()))","(()())","(())()","()(())","()()()"]
print(output, answer, sorted(answer) == sorted(output))
