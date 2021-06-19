from typing import List

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = 0
        flip_list_zero = [0]
        for i in s:
            if i =='1':
                count+=1
            flip_list_zero.append(count)
        flip_list_one = [0]
        count = 0
        for i in s[::-1]:
            if i == '0':
                count+=1
            flip_list_one.append(count)
        flip_list_one = flip_list_one[::-1]
        return min(map(operator.add,flip_list_zero,flip_list_one))

sol = Solution()

print(sol.minFlipsMonoIncr())