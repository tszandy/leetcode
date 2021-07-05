import heapq
from typing import List


class MaxHeap:
    def __init__(self,data):
        self.data = list(map(lambda x:-x,data))
        heapq.heapify(self.data)

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)