from typing import List
import numpy as np

class Solution:
    def countVowelStrings(self, n: int) -> int:
        A = np.array([[1,1,1,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,0,1,1],[0,0,0,0,1]])
        return np.linalg.matrix_power(A,n)[0].sum()
        

sol = Solution()

print(sol.countVowelStrings())