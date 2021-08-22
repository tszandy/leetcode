from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heapq = [1]
        ugly_nums = set()
        repeat_set = set()
        while len(ugly_nums)!=n:
            min_num = heappop(heapq)
            ugly_nums.add(min_num)
            if min_num*2 not in repeat_set:
                heappush(heapq,min_num*2)
                repeat_set.add(min_num*2)
            if min_num*3 not in repeat_set:
                heappush(heapq,min_num*3)
                repeat_set.add(min_num*3)
            if min_num*5not in repeat_set:
                heappush(heapq,min_num*5)
                repeat_set.add(min_num*5)
        return sorted(list(ugly_nums))[-1]

sol = Solution()

print(sol.nthUglyNumber())