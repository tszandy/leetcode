from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        return_list = [[s[0]]]
        if n == 1:            
            return return_list
        for i in range(1,n):
            next_list = []
            for char_list in return_list:
                next_list.append(char_list+[s[i]])
                if char_list[-1]==s[i]:
                    next_list.append(char_list[:])
                    next_list[-1][-1]+=s[i]
                if len(char_list)>=2 and char_list[-2]==s[i]:
                    next_list.append(char_list[:])
                    r = next_list[-1].pop()
                    l = next_list[-1].pop()
                    next_list[-1].append(l+r+s[i])
            return_list = next_list
        return return_list

sol = Solution()


# input
s = "aab"
# output
output = sol.partition(s)
# answer
answer = [["a","a","b"],["aa","b"]]
print(output, answer, answer == output)

# input
s = "a"
# output
output = sol.partition(s)
# answer
answer = [["a"]]
print(output, answer, answer == output)

# input
s = "aabacjfdjj"
# output
output = sol.partition(s)
# answer
answer = [["a","a","b","a","c","j","f","d","j","j"],["a","a","b","a","c","j","f","d","jj"],["a","aba","c","j","f","d","j","j"],["a","aba","c","j","f","d","jj"],["aa","b","a","c","j","f","d","j","j"],["aa","b","a","c","j","f","d","jj"]]
print(output, answer, answer == output)
