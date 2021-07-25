from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return_list = []
        letter_counter = Counter(s)
        distinct_letter_set = set()
        count_letter = 0
        for c in s:
            reset_list = True
            distinct_letter_set.add(c)
            count_letter += 1
            letter_counter[c]-=1
            for dc in distinct_letter_set:
                if letter_counter[dc]!=0:
                    reset_list = False
                    break
            if reset_list:
                return_list.append(count_letter)
                distinct_letter_set = set()
                count_letter = 0
        return return_list
            

sol = Solution()

# input
s = "a"

# output
output = sol.partitionLabels(s)
# answer
answer = [1]
print(output, answer, answer == output)

# input
s = "ab"

# output
output = sol.partitionLabels(s)
# answer
answer = [1,1]
print(output, answer, answer == output)

# input
s = "ababcbacadefegdehijhklij"

# output
output = sol.partitionLabels(s)
# answer
answer = [9,7,8]
print(output, answer, answer == output)

# input
s = "eccbbbbdec"

# output
output = sol.partitionLabels(s)
# answer
answer = [10]
print(output, answer, answer == output)
