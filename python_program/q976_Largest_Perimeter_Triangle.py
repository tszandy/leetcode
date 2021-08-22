from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        max_perimeter = 0
        for i in range(len(nums)-2):
            j=i+1
            k=j+1
            x,y,z = nums[i],nums[j],nums[k]
            if self.none_zero_triangle(z,y,x) and (x+y+z)>max_perimeter:
                max_perimeter = (x+y+z)
        return max_perimeter
    def none_zero_triangle(self, a:int,b:int,c:int)->bool:
        return c<(a+b)

sol = Solution()

print(sol.largestPerimeter())