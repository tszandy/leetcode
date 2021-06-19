from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        points_length = len(points)
        for i in points[:-2]:
            for j in points[1:-1]:
                for k in points[2:]:
                    calculate_area = self.area(i,j,k)
                    if max_area<calculate_area:
                        max_area = calculate_area
        return max_area
    
    def area(self, x:List[int],y:List[int],z:List[int])->float:
        return abs((x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-x[1]*y[0]-y[1]*z[0]-z[1]*x[0])/2)

sol = Solution()

print(sol.largestTriangleArea())