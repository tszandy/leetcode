from typing import List

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num <0:
            return '-'+self.convertToBase7(-num)
        base = 1
        while base*7<=num:
            base*=7
        
        output = ''
        while base != 0:
            output+=str(num//base)
            num %=base
            base //=7
        return output

sol = Solution()

print(sol.convertToBase7())