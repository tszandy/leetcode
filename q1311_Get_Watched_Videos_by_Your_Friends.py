from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friend_list = []
        friend_set = set([id])
        visited_friend_set = set()
        for _ in range(level):
            visited_friend_set = set.union(visited_friend_set, friend_set)
            friend_set = set.union(*list(map(lambda x:set(friends[x]),friend_set)))
            friend_set = set.difference(friend_set,visited_friend_set)
            if len(friend_set)==0:
                return []
        movie_list = sum(list(map(lambda x:watchedVideos[x],friend_set)),[])
        movie_counter = Counter(movie_list)
        movies,_ = zip(*sorted(list(movie_counter.items()),key = lambda x:(x[1],x[0])))
        return list(movies)

sol = Solution()


# input
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
# output
output = sol.watchedVideosByFriends(watchedVideos, friends, id, level)
# answer
answer = ["B","C"] 
print(output, answer, answer == output)

# input
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2
# output
output = sol.watchedVideosByFriends(watchedVideos, friends, id, level)
# answer
answer = ["D"] 
print(output, answer, answer == output)

# input
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 3
# output
output = sol.watchedVideosByFriends(watchedVideos, friends, id, level)
# answer
answer = [] 
print(output, answer, answer == output)

