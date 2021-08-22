from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = float("inf")
        sell_price = float("-inf")
        for price in prices:
            if buy_price > price and sell_price ==float("-inf"):
                buy_price = price
                continue
            if sell_price <= price:
                sell_price = price
                continue
            else:
                profit += sell_price-buy_price
                buy_price = price
                sell_price =float("-inf")
        if sell_price != float("-inf"):
            profit += sell_price-buy_price
            
        return profit

sol = Solution()


# input
prices = [7,1,5,3,6,4]
# output
output = sol.maxProfit(prices)
# answer
answer = 7
print(output, answer, answer == output)

# input
prices = [1,2,3,4,5]
# output
output = sol.maxProfit(prices)
# answer
answer = 4
print(output, answer, answer == output)

# input
prices = [7,6,4,3,1]
# output
output = sol.maxProfit(prices)
# answer
answer = 0
print(output, answer, answer == output)

# input
prices = [4432,123,4,12,45,0,456,654,2,546,6,3]
# output
output = sol.maxProfit(prices)
# answer
answer = 1239
print(output, answer, answer == output)

# input
prices = [0,0,3,3,1,1,4432,123,4,12,45,0,456,654,2,546,6,3]
# output
output = sol.maxProfit(prices)
# answer
answer = 5673
print(output, answer, answer == output)
