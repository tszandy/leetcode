from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        long_com_sub_seq = self.get_longestCommonSubsequence(str1,str2)
        n = len(long_com_sub_seq)
        n_s_1 = len(str1)
        n_s_2 = len(str2)

        string_1_left_index = 0
        string_2_left_index = 0
        return_str = ""
        for i in range(n):
            comm_sub_char = long_com_sub_seq[i]

            while string_1_left_index<n_s_1 and str1[string_1_left_index]!=comm_sub_char:
                return_str+=str1[string_1_left_index]
                string_1_left_index+=1
            if string_1_left_index == n_s_1:
                return return_str+str2[string_2_left_index:]

            while string_2_left_index<n_s_2 and str2[string_2_left_index]!=comm_sub_char:
                return_str+=str2[string_2_left_index]
                string_2_left_index+=1

            return_str+=comm_sub_char        
            string_1_left_index+=1
            string_2_left_index+=1
        return return_str+str1[string_1_left_index:]+str2[string_2_left_index:]


    def get_longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp =defaultdict(list)
        dp[(-1,-1)].append((0,(-1,-1)))
        for i in range(m):
            dp[(i,-1)].append((0,(-1,-1)))
        for i in range(n):
            dp[(-1,i)].append((0,(-1,-1)))

        for i in range(m):
            c1 = text1[i]
            for j in range(n):
                c2 = text2[j]
                if c1==c2:
                    dp[(i,j)].append((dp[(i-1,j-1)][0][0]+1,(i-1,j-1)))
                else:
                    if dp[(i-1,j)][0][0] > dp[(i,j-1)][0][0]:
                        dp[(i,j)].append((dp[(i-1,j)][0][0],(i-1,j)))
                    else:
                        dp[(i,j)].append((dp[(i,j-1)][0][0],(i,j-1)))

        max_sub_count = 0
        max_sub_index = (None,None)
        for i in range(m):
            for j in range(n):
                if max_sub_count<dp[(i,j)][0][0]:
                    max_sub_count,max_sub_index = dp[(i,j)][0][0],(i,j)
        return_str = ""
        while max_sub_count:
            next_sub_index = dp[max_sub_index][0][1]
            next_sub_count = dp[next_sub_index][0][0]
            if next_sub_count != max_sub_count:
                return_str+=text1[max_sub_index[0]]
            max_sub_count,max_sub_index = next_sub_count,next_sub_index
        return return_str[::-1]

sol = Solution()


# input
str1 = "abac"

str2 = "cab"

# output
output = sol.shortestCommonSupersequence(str1,str2)
# answer
answer = "cabac"
print(output, answer, answer == output)


# input
str1 = "abacdfdsfadsa"

str2 = "casdfsgdfsb"

# output
output = sol.shortestCommonSupersequence(str1,str2)
# answer
answer = "abacasdfdsfagdfsab"
print(output, answer, answer == output)

# input
str1 = "aaaaaaaa"

str2 = "aaaaaaaa"

# output
output = sol.shortestCommonSupersequence(str1,str2)
# answer
answer = "aaaaaaaa"
print(output, answer, answer == output)


# input
str1 = "aaaaaasdfdaadggas"

str2 = "aaaaaadfsaefaaa"

# output
output = sol.shortestCommonSupersequence(str1,str2)
# answer
answer = "aaaaaaaa"
print(output, answer, answer == output)

