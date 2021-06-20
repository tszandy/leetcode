from typing import List

class Solution:
    def minimumBoxes(self, n: int) -> int:
        count_boxes_touching_floor=0
        i=1
        while n-(i*(i+1))/2>=0:
            count_boxes_touching_floor+=i
            n-=(i*(i+1))/2
            i+=1
        count_boxes_touching_floor+=math.ceil(sqrt(2*n+1/4)-1/2)
        return count_boxes_touching_floor

sol = Solution()

print(sol.minimumBoxes())