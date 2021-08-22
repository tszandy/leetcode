from typing import List

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_list = num1.split('+') 
        num2_list = num2.split('+') 
        c1 = (int(num1_list[0]),int(num1_list[1][:-1]))
        c2 = (int(num2_list[0]),int(num2_list[1][:-1]))
        
        output = (c1[0]*c2[0]-c1[1]*c2[1],c1[1]*c2[0]+c1[0]*c2[1])
        return "{}+{}i".format(*output)

sol = Solution()

print(sol.complexNumberMultiply())