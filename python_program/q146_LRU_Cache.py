from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class LRUCache:

    def __init__(self, capacity: int):
        self.store_list = []
        self.store_dict = {}
        self.capacity = capacity
        self.count_elem = 0

    def get(self, key: int) -> int:
        if key in self.store_list:
            self.store_list.pop(self.store_list.index(key))
            self.store_list.append(key)
            return self.store_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store_list:
            self.store_list.pop(self.store_list.index(key))
            self.store_list.append(key)
            self.store_dict[key] = value
        elif self.count_elem<self.capacity:
            self.store_list.append(key)
            self.store_dict[key]=value
            self.count_elem+=1
        else:
            elem = self.store_list.pop(0)
            del self.store_dict[elem]
            self.store_list.append(key)
            self.store_dict[key] = value
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

sol = Solution()

# input
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
