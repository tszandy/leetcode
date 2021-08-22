from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

import heapq
class MaxHeap:
    def __init__(self,data):
        self.data = list(map(lambda x:-x,data))
        heapq.heapify(self.data)
    def __init__(self):
        self.data = []

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    def size(self):
        return len(self.data)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_heap = MaxHeap()
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
                max_heap.push(sell_price-buy_price)
                buy_price = price
                sell_price =float("-inf")
        if sell_price != float("-inf"):
            max_heap.push(sell_price-buy_price)
            
        if max_heap.size() >=2:
            profit+=max_heap.pop()
            profit+=max_heap.pop()
        elif max_heap.size()==1:
            profit+=max_heap.pop()
        
        return profit

sol = Solution()


# input
prices = [3,3,5,0,0,3,1,4,1,13]
# output
output = sol.maxProfit(prices)
# answer
answer = 6
print(output, answer, answer == output)

# input
prices = [3,3,5,0,0,3,1,4]
# output
output = sol.maxProfit(prices)
# answer
answer = 6
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
prices = [1]
# output
output = sol.maxProfit(prices)
# answer
answer = 0
print(output, answer, answer == output)
