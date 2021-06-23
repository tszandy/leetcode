from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        return_int = 0
        current_char = chars[0]
        count = 1
        for char in chars[1:]:
            if char != current_char:
                chars[return_int] = current_char
                return_int +=1
                if count == 1:
                    current_char = char
                else:
                    for i in str(count):
                        chars[return_int] = i
                        return_int +=1
                    current_char = char
                count = 1
            else:
                count += 1
        
        chars[return_int] = current_char
        return_int +=1
        if count == 1:
            current_char = char
        else:
            for i in str(count):
                chars[return_int] = i
                return_int +=1
            current_char = char
        count = 1

        return return_int

sol = Solution()


# input
chars = ["a","a","b","b","c","c","c"]
# output
output = sol.compress(chars)
# answer
answer = 6
print(output, answer, answer == output)

# input
chars = ["a"]
# output
output = sol.compress(chars)
# answer
answer = 1
print(output, answer, answer == output)

# input
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# output
output = sol.compress(chars)
# answer
answer = 4
print(output, answer, answer == output)

# input
chars = ["a","a","a","b","b","a","a"]
# output
output = sol.compress(chars)
# answer
answer = 6
print(output, answer, answer == output)
