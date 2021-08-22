from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend<0:
            return -self.neg_divide(-dividend,divisor)
        if divisor<0:
            return -self.neg_divide(dividend,-divisor)

        result = 0
        divisor_list = []
        divisor_multiplier = 1
        while divisor<=dividend:
            divisor_list.append((divisor,divisor_multiplier))
            divisor+=divisor
            divisor_multiplier += divisor_multiplier

        while divisor_list:
            divisor,divisor_multiplier = divisor_list.pop()
            if dividend >= divisor:
                dividend -= divisor

                result += divisor_multiplier
        if result >=2147483647:return 2147483647
        return result

    def neg_divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor<0:
            return -self.divide(dividend,-divisor)

        result = 0
        divisor_list = []
        divisor_multiplier = 1
        while divisor<=dividend:
            divisor_list.append((divisor,divisor_multiplier))
            divisor+=divisor
            divisor_multiplier += divisor_multiplier

        while divisor_list:
            divisor,divisor_multiplier = divisor_list.pop()
            if dividend >= divisor:
                dividend -= divisor

                result += divisor_multiplier
        return result



sol = Solution()


# input
dividend = 10
divisor = 3
# output
output = sol.divide(dividend,divisor)
# answer
answer = 3
print(output,answer,answer == output)

# input
dividend = 7
divisor = -3
# output
output = sol.divide(dividend,divisor)
# answer
answer = -2
print(output,answer,answer == output)

# input
dividend = 0
divisor = 1
# output
output = sol.divide(dividend,divisor)
# answer
answer = 0
print(output,answer,answer == output)

# input
dividend = 1
divisor = 1
# output
output = sol.divide(dividend,divisor)
# answer
answer = 1
print(output,answer,answer == output)

# input
dividend = 1
divisor = 2
# output
output = sol.divide(dividend,divisor)
# answer
answer = 0
print(output,answer,answer == output)

# input
dividend = 214748366
divisor = 1
# output
output = sol.divide(dividend,divisor)
# answer
answer = 214748366
print(output,answer,answer == output)

# input
dividend = -2147483648
divisor = -1
# output
output = sol.divide(dividend,divisor)
# answer
answer = 2147483647
print(output,answer,answer == output)

# input
dividend = -2147483648
divisor = 1
# output
output = sol.divide(dividend,divisor)
# answer
answer = -2147483648
print(output,answer,answer == output)

