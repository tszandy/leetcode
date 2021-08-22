from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = {}
        key_set = set()
        value_set = set()
        for c1,c2 in zip(s,t):
            if c1 not in key_set and c2 not in value_set:
                map_dict[c1]=c2
                key_set.add(c1)
                value_set.add(c2)
                continue
            if c1 in key_set and c2 in value_set:
                if map_dict[c1]!=c2:
                    return False
                continue
            # if c1 in key_set and c2 not in value_set:
            #     return False
            # if c1 not in key_set and c2 in value_set:
            #     return False
            return False
        return True

sol = Solution()


# input
s = "egg"
t = "add"
# output
output = sol.isIsomorphic(s,t)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "foo"
t = "bar"
# output
output = sol.isIsomorphic(s,t)
# answer
answer = False
print(output, answer, answer == output)

# input
s = "paper"
t = "title"# output
output = sol.isIsomorphic(s,t)
# answer
answer = True
print(output, answer, answer == output)
