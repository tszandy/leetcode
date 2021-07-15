from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def good_counter():
            for i in letter_counter:
                if letter_counter[i]<0:
                    return False
            return True

        letter_counter = Counter(letters)
        char_to_score = lambda x:score[ord(x)-97]
        n = len(words)
        max_score = [0]

        def backtracking(index,score):
            if not good_counter():
                return
            else:
                max_score[0] = max(max_score[0],score)
            for i in range(index,n):
                word = words[i]
                count_score = 0
                for c in word:
                    letter_counter[c]-=1
                    count_score += char_to_score(c)
                backtracking(i+1,score+count_score)
                for c in word:
                    letter_counter[c]+=1
            
        
        backtracking(0,0)
        return max_score[0]


sol = Solution()


# input
words = ["dog","cat","dad","good"]

letters = ["a","a","c","d","d","d","g","o","o"]

score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

# output
output = sol.maxScoreWords(words,letters,score)
# answer
answer = 23
print(output, answer, answer == output)

# input
words = ["xxxz","ax","bx","cx"]

letters = ["z","a","b","c","x","x","x"]

score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

# output
output = sol.maxScoreWords(words,letters,score)
# answer
answer = 27
print(output, answer, answer == output)

# input
words = ["leetcode"]

letters = ["l","e","t","c","o","d"]

score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

# output
output = sol.maxScoreWords(words,letters,score)
# answer
answer = 0
print(output, answer, answer == output)
