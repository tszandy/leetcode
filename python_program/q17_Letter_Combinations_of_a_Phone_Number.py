from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        digits_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        return_list = list(digits_map[digits[0]])
        for digit in digits[1:]:
            next_return_list = []
            for c in digits_map[digit]:
                for string in return_list:            
                    next_return_list.append(string+c)    
            return_list = next_return_list
        return return_list

sol = Solution()


# input
digits = "23"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = ""
# output
output = sol.letterCombinations(digits)
# answer
answer = []
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "2"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["a","b","c"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "3"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["d","e","f"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "4"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["g","h","i"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "5"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["j","k","l"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "6"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["m","n","o"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "7"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["p","q","r","s"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "8"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["t","u","v"]
print(output, answer, sorted(answer) == sorted(output))

# input
digits = "9"
# output
output = sol.letterCombinations(digits)
# answer
answer = ["w","x","y","z"]
print(output, answer, sorted(answer) == sorted(output))
