from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_num = min(len(word1),len(word2))
        return "".join(map(lambda x:x[0]+x[1],zip(word1[:min_num],word2[:min_num])))+word1[min_num:]+word2[min_num:]

sol = Solution()

word1 = "abc"
word2 = "pqr"
print(sol.mergeAlternately(word1,word2))

word1 = "ab"
word2 = "pqrs"
print(sol.mergeAlternately(word1,word2))

word1 = "abcd"
word2 = "pq"
print(sol.mergeAlternately(word1,word2))
