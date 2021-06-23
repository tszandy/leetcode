from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def countSegments(self, s: str) -> int:
        return len(list(filter(lambda x:x!="",s.split(" "))))

sol = Solution()


# input
s = "Hello, my name is John"
# output
output = sol.countSegments(s)
# answer
answer = 5
print(output, answer, answer == output)

# input
s = "Hello"
# output
output = sol.countSegments(s)
# answer
answer = 1
print(output, answer, answer == output)

# input
s = "love live! mu'sic forever"
# output
output = sol.countSegments(s)
# answer
answer = 4
print(output, answer, answer == output)

# input
s = ""
# output
output = sol.countSegments(s)
# answer
answer = 0
print(output, answer, answer == output)
