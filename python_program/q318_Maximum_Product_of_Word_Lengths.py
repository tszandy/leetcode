from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_value = 0
        n = len(words)
        for i in range(n-1):
            set_str_1 = set(words[i])
            str_1_length = len(words[i])
            for j in range(i+1,n):
                set_str_2 = set(words[j])
                str_2_length = len(words[j])
                if len(set.intersection(set_str_1,set_str_2))==0 and str_1_length*str_2_length>max_value:
                    max_value = str_1_length*str_2_length
        return max_value

sol = Solution()


# input
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# output
output = sol.maxProduct(words)
# answer
answer = 16
print(output, answer, answer == output)

# input
words = ["a","ab","abc","d","cd","bcd","abcd"]
# output
output = sol.maxProduct(words)
# answer
answer = 4
print(output, answer, answer == output)

# input
words = ["a","aa","aaa","aaaa"]
# output
output = sol.maxProduct(words)
# answer
answer = 0
print(output, answer, answer == output)

# input
words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
# output
output = sol.maxProduct(words)
# answer
answer = 15
print(output, answer, answer == output)
