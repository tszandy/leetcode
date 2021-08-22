from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def is_palindrome(s):
            n = len(s)
            if n == 1:
                return True
            for i in range(n//2+1):
                if s[i]!=s[n-1-i]:
                    return False
            return True

        @lru_cache(None)
        def min_cut(s):
            n = len(s)
            if is_palindrome(s):
                return 0
            min_count = float("inf")
            for i in range(n-1):
                left = min_cut(s[:i+1])
                right = min_cut(s[i+1:])
                min_count = min(min_count,1+left+right)
            return min_count
        return min_cut(s)

    def minCut(self, s: str) -> int:
        n = len(s)
        @lru_cache(None)
        def is_palindrome(l,r):
            if l ==r:
                return True
            m = (l+r)//2
            for i in range(m-l+1):
                if s[l+i]!= s[r-i]:
                    return False
            return True

        @lru_cache(None)
        def min_cut(l,r):
            if is_palindrome(l,r):
                return 0
            min_count = float("inf")
            for i in range(l,r):
                left = min_cut(l,i)
                right = min_cut(i+1,r)
                min_count = min(min_count,1+left+right)
            return min_count
        return min_cut(0,n-1)

sol = Solution()


# input
s = "aab"

# output
output = sol.minCut(s)
# answer
answer = 1
print(output, answer, answer == output)

# input
s = "a"

# output
output = sol.minCut(s)
# answer
answer = 0
print(output, answer, answer == output)

# input
s = "ab"

# output
output = sol.minCut(s)
# answer
answer = 1
print(output, answer, answer == output)

# input
s = "aabaabaabaaaaabaaaaabaaaababaabbbbabaabaab"

# output
output = sol.minCut(s)
# answer
answer = 4
print(output, answer, answer == output)

# input
s = "aabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaab"

# output
output = sol.minCut(s)
# answer
answer = 19
print(output, answer, answer == output)

# input
s = "aabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaabaabaabaabaaaaabaaaaabaaahfjkdhaajsjsjdhhhhfhdhshshjfababaabbbbabaabaab"

# output
output = sol.minCut(s)
# answer
answer = 4
print(output, answer, answer == output)
