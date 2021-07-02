from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return False
        else:
            self.count += 1
            self.set.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.set:
            return False
        else:
            self.count -= 1
            self.set.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

sol = RandomizedSet()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
