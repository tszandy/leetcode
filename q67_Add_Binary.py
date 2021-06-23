from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

sol = Solution()

print(sol.func())