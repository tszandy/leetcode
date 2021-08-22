from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        int_to_char = {i:chr(97+i) for i in range(26)}
        char_to_int = {chr(97+i):i for i in range(26)}
        s_int_array = np.array(list(map(lambda x:char_to_int[x],s)))
        shift_array = np.cumsum(shifts[::-1])[::-1]%26
        return "".join(map(lambda x:int_to_char[x],(s_int_array+shift_array)%26))

sol = Solution()


# input
s = "abc"
shifts = [3,5,9]
# output
output = sol.shiftingLetters(s,shifts)
# answer
answer = "rpl"
print(output, answer, answer == output)

