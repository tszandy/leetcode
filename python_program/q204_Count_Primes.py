from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def countPrimes(self, n: int) -> int:        
        if n<2:
            return 0
        
        is_prime=[1]*n
        is_prime[0]=is_prime[1]=0
        
        for i in range(2,int(sqrt(n))+1):
            if is_prime[i]:
                is_prime[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
        return sum(is_prime)


    def countPrimes_1(self, n: int) -> int:
        primes = []
        bool_prime = True
        for i in range(2,n):
            for prime in primes:
                if i%prime ==0:
                    bool_prime = False
                    break
            if bool_prime:
                primes.append(i)
            bool_prime = True
        return len(primes)

sol = Solution()


# input
n = 10
# output
output = sol.countPrimes(n)
# answer
answer = 4
print(output, answer, answer == output)

# input
n = 0
# output
output = sol.countPrimes(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 1
# output
output = sol.countPrimes(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 2
# output
output = sol.countPrimes(n)
# answer
answer = 0
print(output, answer, answer == output)

# input
n = 3
# output
output = sol.countPrimes(n)
# answer
answer = 1
print(output, answer, answer == output)

# input
n = 499979
# output
output = sol.countPrimes(n)
# answer
answer = 41537
print(output, answer, answer == output)
