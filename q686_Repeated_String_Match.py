from typing import List
from collections import Counter
from math import *

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        set_a = set(a)
        for i in b:
            if i not in set_a:
                return -1
                
        length_a = len(a)
        counter_a = Counter(a)
        counter_b = Counter(b)
        max_repeat_count = max(map(lambda x:ceil(counter_b[x]/counter_a[x]),counter_b.keys()))+2
        repeat_string = a*max_repeat_count
        
        if b not in repeat_string:return -1
        
        while b in repeat_string:
            max_repeat_count -=1
            repeat_string = repeat_string[:-length_a]
        
        return max_repeat_count+1

sol = Solution()


a = "abcd"
b = "cdabcdab"
print(sol.repeatedStringMatch(a, b))

a = "a"
b = "aa"
print(sol.repeatedStringMatch(a, b))

a = "a"
b = "a"
print(sol.repeatedStringMatch(a, b))


a = "abc"
b = "wxyz"
print(sol.repeatedStringMatch(a, b))


