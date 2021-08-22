from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')

sol = Solution()

print(sol.func())