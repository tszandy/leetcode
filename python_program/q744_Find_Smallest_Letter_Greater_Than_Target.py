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
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[(bisect_right(letters,target)%len(letters))]


sol = Solution()

# input
letters = ["c","f","j"]

target = "a"

# output
output = sol.nextGreatestLetter(letters,target)
# answer
answer = "c"

print(output, answer, answer == output)

# input
letters = ["c","f","j"]

target = "c"

# output
output = sol.nextGreatestLetter(letters,target)
# answer
answer = "f"

print(output, answer, answer == output)

# input
letters = ["c","f","j"]

target = "d"

# output
output = sol.nextGreatestLetter(letters,target)
# answer
answer = "f"

print(output, answer, answer == output)

# input
letters = ["c","f","j"]

target = "g"

# output
output = sol.nextGreatestLetter(letters,target)
# answer
answer = "j"

print(output, answer, answer == output)

# input
letters = ["c","f","j"]

target = "j"

# output
output = sol.nextGreatestLetter(letters,target)
# answer
answer = "c"
print(output, answer, answer == output)
