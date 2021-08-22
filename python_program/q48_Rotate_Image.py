from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
            
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j],matrix[j][-i-1],matrix[-i-1][-j-1],matrix[-j-1][i] = matrix[-j-1][i],matrix[i][j],matrix[j][-i-1],matrix[-i-1][-j-1]
        return matrix

sol = Solution()


# input
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# output
output = sol.rotate(matrix)
# answer
answer = [[7,4,1],[8,5,2],[9,6,3]]
print(output, answer, answer == output)

# input
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# output
output = sol.rotate(matrix)
# answer
answer = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
print(output, answer, answer == output)

# input
matrix = [[1]]
# output
output = sol.rotate(matrix)
# answer
answer = [[1]]
print(output, answer, answer == output)

# input
matrix = [[1,2],[3,4]]
# output
output = sol.rotate(matrix)
# answer
answer = [[3,1],[4,2]]
print(output, answer, answer == output)
