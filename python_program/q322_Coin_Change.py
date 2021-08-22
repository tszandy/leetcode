from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
#dp 
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[amount] != float("inf"):
            return dp[amount]
        else:
            return -1

#backtracking on reverse coins optimal return best answer time limited exceeded
    def coinChange_2(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        count_coin = [0]
        optimal_count_coin = [float("inf")]
        coins = sorted(coins)[::-1]
        
        def backtracking(count_amount,target_amount,index):
            if count_amount == target_amount and count_coin[0]<optimal_count_coin[0]:
                optimal_count_coin[0] = count_coin[0]
                return 
            if count_amount > target_amount:
                return 
            for i in range(index,n):
                coin = coins[i]
                count_coin[0]+=1
                backtracking(count_amount+coin,target_amount,i)
                count_coin[0]-=1
            
        backtracking(0,amount,0)
        if optimal_count_coin[0]!= float("inf"):
            return optimal_count_coin[0]
        else:
            return -1

#backtracking on reverse coins not optimal return one answer
    def coinChange_1(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        count_coin = [0]
        coins = sorted(coins)[::-1]
        
        def backtracking(count_amount,target_amount,index):
            if count_amount == target_amount:
                return count_coin[0]
            if count_amount > target_amount:
                return 
            for i in range(index,n):
                coin = coins[i]
                count_coin[0]+=1
                result = backtracking(count_amount+coin,target_amount,i)
                if result:
                    return result
                count_coin[0]-=1
            
        result = backtracking(0,amount,0)
        if result:
            return result
        else:
            return -1

sol = Solution()


# input
coins = [1,2,5]
amount = 11
# output
output = sol.coinChange(coins,amount)
# answer
answer = 3
print(output, answer, answer == output)

# input
coins = [2]
amount = 3
# output
output = sol.coinChange(coins,amount)
# answer
answer = -1
print(output, answer, answer == output)

# input
coins = [1]
amount = 0
# output
output = sol.coinChange(coins,amount)
# answer
answer = 0
print(output, answer, answer == output)

# input
coins = [1]
amount = 1
# output
output = sol.coinChange(coins,amount)
# answer
answer = 1
print(output, answer, answer == output)

# input
coins = [1]
amount = 2
# output
output = sol.coinChange(coins,amount)
# answer
answer = 2
print(output, answer, answer == output)

# input
coins = [1,2,5]
amount = 9518
# output
output = sol.coinChange(coins,amount)
# answer
answer = 1905
print(output, answer, answer == output)

# input
coins = [186,419,83,408]
amount = 6249
# output
output = sol.coinChange(coins,amount)
# answer
answer = 20
print(output, answer, answer == output)
