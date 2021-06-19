from typing import List

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        leftIntegerPart = ''
        leftNonRepeatingPart = ''
        leftRepeatingPart = ''
        rightIntegerPart = ''
        rightNonRepeatingPart = ''
        rightRepeatingPart = ''
        
        if '(' in s:
            leftRepeatingPart = s.split('(')[1][:-1]
        if '.' in s:
            leftIntegerPart, leftNonRepeatingPart = s.split('(')[0].split(".")
        else:
            leftIntegerPart = s

        if '(' in t:
            rightRepeatingPart = t.split('(')[1][:-1]
        if '.' in t:
            rightIntegerPart, rightNonRepeatingPart = t.split('(')[0].split(".")
        else:
            rightIntegerPart = t
        
        left_simple_frac = self.get_simple_frac(leftIntegerPart,leftNonRepeatingPart,leftRepeatingPart)
        right_simple_frac = self.get_simple_frac(rightIntegerPart,rightNonRepeatingPart,rightRepeatingPart)

        return left_simple_frac == right_simple_frac            
    
    
    def get_simple_frac(self, IntegerPart:str, NonRepeatingPart:str,RepeatingPart:str) -> tuple:
        
        NonRepeating_count_0 = 10**len(NonRepeatingPart)
        Repecting_count_0 = 10**len(RepeatingPart)
        if NonRepeatingPart:
            NonRepeating_frac = (int(IntegerPart)*NonRepeating_count_0+int(NonRepeatingPart),NonRepeating_count_0)
        else:
            NonRepeating_frac = (int(IntegerPart)*NonRepeating_count_0,NonRepeating_count_0)
            
        if RepeatingPart:
            Repeating_frac = (int(RepeatingPart),NonRepeating_count_0*(Repecting_count_0-1))
        
        if RepeatingPart:
            frac = self.frac_add(NonRepeating_frac,Repeating_frac)
        else:
            frac = NonRepeating_frac
        frac_gcd = self.gcd(*frac)
        return (int(frac[0]/frac_gcd),int(frac[1]/frac_gcd))
        
    def gcd(self,a:int,b:int)->int:
        if b == 0:
            return a
        if a<b:
            return self.gcd(b,a)
        return self.gcd(b,a-(a//b)*b)
            
    def frac_add(self, a:tuple,b:tuple)->tuple:
        return (a[0]*b[1]+a[1]*b[0],a[1]*b[1])

sol = Solution()

print(sol.isRationalEqual())
