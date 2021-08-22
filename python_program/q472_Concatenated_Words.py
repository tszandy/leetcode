from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        return_list = []
        if "" in words:
            words.remove("")
        if len(words)==0:
            return return_list
        words_set = set(words)
        
        for word in words:
            dp = {0:0}
            word_index = [0]
            for i in range(len(word)+1):
                dp[i] = 0
                for index in list(word_index):
                    if word[index:i] in words_set:
                        word_index.append(i)
                        dp[i] = max(dp[i],dp[index]+1)
            if dp[len(word)]>1:
                return_list.append(word)
        return return_list

sol = Solution()

# input
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

# output
output = sol.findAllConcatenatedWordsInADict(words)
# answer
answer = ["catsdogcats","dogcatsdog","ratcatdogcat"]
print(output, answer, answer == output)

# input
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","catcat"]

# output
output = sol.findAllConcatenatedWordsInADict(words)
# answer
answer = ["catsdogcats","dogcatsdog","ratcatdogcat","catcat"]
print(output, answer, answer == output)

# input
words = ["cat","dog","catdog"]

# output
output = sol.findAllConcatenatedWordsInADict(words)
# answer
answer = ["catdog"]
print(output, answer, answer == output)

# input
words = [""]

# output
output = sol.findAllConcatenatedWordsInADict(words)
# answer
answer = []
print(output, answer, answer == output)

# input
words = ["a",""]

# output
output = sol.findAllConcatenatedWordsInADict(words)
# answer
answer = []
print(output, answer, answer == output)
