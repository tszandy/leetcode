from typing import List

import numpy as np
import numpy.linalg as LA
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1 = np.array(p1)
        p2 = np.array(p2)
        p3 = np.array(p3)
        p4 = np.array(p4)
        
        start = p1
        
        dia_bool = False
        if (p2-p1).dot(p3-p1)==0:
            if dia_bool:
                return False
            dia = p4
            side_1 = p2
            side_2 = p3
            dia_bool = True
            
        if (p2-p1).dot(p4-p1)==0:
            if dia_bool:
                return False
            dia = p3
            side_1 = p2
            side_2 = p4
            dia_bool = True
            
        if (p3-p1).dot(p4-p1)==0:
            if dia_bool:
                return False
            dia = p2
            side_1 = p3
            side_2 = p4
            dia_bool = True
                    
        if not (p2-p1).dot(p3-p1)==0 and not (p2-p1).dot(p4-p1)==0 and not (p3-p1).dot(p4-p1)==0:
            return False
    
        l1 = start-side_1
        l2 = start-side_2
        l3 = dia-side_1
        l4 = dia-side_2
        if LA.norm(l1) == LA.norm(l2) and LA.norm(l2) == LA.norm(l3) and LA.norm(l3) == LA.norm(l4):
            return True
        else:
            return False

sol = Solution()

print(sol.validSquare())
