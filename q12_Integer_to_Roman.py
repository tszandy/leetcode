from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        output = ''
        thresholds = [1000,900 ,500,400 ,100,90  ,50 ,40  ,10 ,9   ,5  ,4   ,1  ]
        romans     = ["M" ,"CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        for threshold,roman in zip(thresholds,romans):
            while num>=threshold:
                output += roman
                num    -= threshold
        return output

sol = Solution()

print(sol.intToRoman())