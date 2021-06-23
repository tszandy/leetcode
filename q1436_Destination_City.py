from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        depart_city,dest_city = zip(*paths)
        depart_city_set = set(depart_city)
        dest_city_set = set(dest_city)
        
        for city in dest_city:
            if city not in depart_city_set:
                return city

sol = Solution()

print(sol.destCity())