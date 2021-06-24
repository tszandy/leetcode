from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant_name = ""
        index_sum = len(list1)+len(list2)
        list_2_index_dict = {e:i for i,e in enumerate(list2)}
        return_list = []
        for index,restaurant in enumerate(list1):
            if restaurant in list_2_index_dict:
                if index_sum ==len(list1)+len(list2):
                    index_sum = list_2_index_dict[restaurant]+index
                    return_list.append(restaurant)
                elif index_sum == list_2_index_dict[restaurant]+index:
                    return_list.append(restaurant)
                else:
                    break
        return return_list

sol = Solution()


# input
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# output
output = sol.findRestaurant(list1,list2)
# answer
answer = ["Shogun"]
print(output, answer, sorted(answer) == sorted(output))

# input
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
# output
output = sol.findRestaurant(list1,list2)
# answer
answer = ["Shogun"]
print(output, answer, sorted(answer) == sorted(output))

# input
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# output
output = sol.findRestaurant(list1,list2)
# answer
answer = ["KFC","Burger King","Tapioca Express","Shogun"]
print(output, answer, sorted(answer) == sorted(output))

# input
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# output
output = sol.findRestaurant(list1,list2)
# answer
answer = ["KFC","Burger King","Tapioca Express","Shogun"]
print(output, answer, sorted(answer) == sorted(output))

# input
list1 = ["KFC"]
list2 = ["KFC"]
# output
output = sol.findRestaurant(list1,list2)
# answer
answer = ["KFC"]
print(output, answer, sorted(answer) == sorted(output))
