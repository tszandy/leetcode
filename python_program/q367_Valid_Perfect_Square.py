from typing import List

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 2
        while i**2<=num:
            
            count = 0
            while num % i == 0:
                count+=1
                num /= i
            if count %2 ==1:
                return False
            i+=1
        if num == 1:
            return True
        return False
        

sol = Solution()

print(sol.isPerfectSquare())