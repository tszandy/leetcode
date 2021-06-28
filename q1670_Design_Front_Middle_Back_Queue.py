from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class FrontMiddleBackQueue:

    def __init__(self):
        self.length = 0
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0,val)
        self.length+=1

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(self.length//2,val)
        self.length+=1
        

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.length+=1

    def popFront(self) -> int:
        if not self.length:
            return -1
        else:
            return_elem = self.queue.pop(0)
            self.length-=1
            return return_elem

    def popMiddle(self) -> int:
        if not self.length:
            return -1
        else:
            return_elem = self.queue.pop((self.length-1)//2)
            self.length-=1
            return return_elem

    def popBack(self) -> int:
        if not self.length:
            return -1
        else:
            self.length-=1
            return self.queue.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

sol = Solution()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
