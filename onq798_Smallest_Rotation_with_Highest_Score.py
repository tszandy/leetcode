from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

import numpy as np
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        nums = np.array(nums)
        range_array = np.array(range(n))
        best_rotation_k = 0
        best_rotation_score = 0
        roll_nums = nums
        for i in range(n):
            current_score = max(best_rotation_score,sum(roll_nums<=range_array))
            if best_rotation_score < current_score:
                best_rotation_score = current_score
                best_rotation_k = i
            roll_nums = np.roll(roll_nums,-1)
        
        return best_rotation_k

sol = Solution()


# input
nums = [2,3,1,4,0]
# output
output = sol.bestRotation(nums)
# answer
answer = 3
print(output, answer, answer == output)

# input
nums = [408,15,591,534,788,426,620,768,200,878,226,826,45,603,615,744,976,859,748,485,177,69,251,278,473,716,943,580,563,825,375,757,752,327,68,43,972,995,772,807,343,440,456,498,510,819,644,104,490,841,482,92,751,637,783,695,936,656,45,93,525,401,895,29,800,715,854,119,93,780,492,48,252,910,656,44,777,452,987,306,816,124,864,998,909,759,170,938,919,668,653,935,933,663,101,453,114,521,900,799,379,141,797,431,164,141,841,706,29,729,255,26,533,969,481,737,384,596,531,973,373,628,750,787,508,13,65,353,810,927,370,281,716,598,893,587,398,707,118,632,95,983,520,887,426,902,709,269,171,657,739,80,937,633,140,198,344,899,273,919,562,95,126,665,148,560,694,523,795,506,712,310,931,819,516,416,42,17,560,434,251,614,832,506,510,491,898,835,811,35,584,469,538,513,217,307,479,900,224,639,282,871,877,822,156,597,39,735,506,628,839,243,235,106,151,170,203,891,746,224,4,581,815,507,78,599,951,231,754,833,108,874,399,344,737,498,897,118,140,671,15,746,560,240,452,114,69,637,707,327,310,234,190,704,729,947,704,37,987,619,182,916,559,558,74,525,443,980,258,731,769,5,126,404,80,693,210,355,814,332,994,449,971,657,712,73,826,46,257,59,832,424,42,814,253,771,890,946,783,142,18,449,27,490,85,302,673,48,773,112,544,771,899,454,136,120,420,986,949,160,649,801,580,866,404,665,86,484,214,904,625,880,79,246,795,302,731,990,482,753,44,869,920,897,450,10,79,909,782,442,923,434,822,643,423,675,600,81,48,347,156,365,791,835,359,604,571,380,907,437,28,862,694,157,158,910,713,749,14,876,824,235,941,696,865,727,335,875,135,94,474,71,592,422,423,681,311,835,209,847,72,471,561,194,945,397,637,503,707,317,605,596,69,838,3,914,627,104,13,242,843,336,850,565,171,545,622,591,645,967,135,234,703,281,156,146,351,654,114,955,438,78,651,715,149,245,496,83,241,19,805,757,497,863,376,488,537,300,862,268,659,732,397,354,393,772,248,692,954,150,591,267,652,229,97,140,184,13,612,855,985,115,193,443,881,597,891,725,108,921,615,181,921,781,225,261,881,764,811,288,954,768,718,100,701,835,761,567,696,596,998,249,982,443,438,813,319,321,983,54,295,614,152,455,80,598,96,846,371,956,421,148,558,673,464,797,906,606,69,545,430,454,821,410,632,876,612,935,82,485,656,873,489,15,844,428,372,68,589,642,468,307,799,314,33,653,280,552,887,452,795,672,418,23,376,145,393,645,860,307,754,910,425,631,544,882,883,204,684,235,194,42,812,235,590,498,827,253,3,812,605,84,405,381,319,878,116,88,518,528,565,506,863,760,278,496,652,303,546,842,399,108,265,315,1,58,87,583,582,831,818,341,168,101,280,138,852,661,762,86,76,536,660,905,824,878,674,242,232,836,844,426,313,884,537,226,761,386,229,777,607,37,820,827,330,653,673,225,576,60,754,509,503,697,111,723,197,693,833,456,210,186,742,728,397,793,549,303,1,664,513,908,218,672,968,762,840,821,928,815,740,227,952,680,541,750,105,267,367,658,574,572,858,519,83,977,437,600,125,74,307,676,192,649,397,870,460,597,813,724,169,67,46,904,817,695,564,117,124,368,74,446,331,263,914,58,553,863,625,74,603,89,938,555,803,256,569,657,621,828,336,103,846,246,602,855,618,198,595,474,860,925,852,176,105,152,250,401,574,514,291,764,506,587,768,861,612,682,908,208,389,336,889,111,111,444,552,687,712,295,684,423,560,398,340,753,953,556,740,244,104,308,426,864,104,707,235,748,890,191,513,378,244,627,73,72,647,5,708,323,789,702,418,270,437,815,700,835,929,750,2,760,505,648,259,941,591,856,824,986,698,633,191,235,531,980,727,527,444,605,504,390,292,833,567,684,992,444,313,26,179,156,125,930,795,517,839,702,482,243,120,384,369,159,642,579,27,30,209,35,636,659,787,734,490,776,9,376,29,833,972,172,83,296,635,193,738,851,487,70,528,895,413,422,732,407,212,719,428,802,739,48,293,615,597,960,622,687,615,291,457,890,259,335,298,934,880,787,19,244,122,597,248,205,420,558,162,440,56,110,168,562,770,228,666,805,640,385,634,366,264,87,387,223,465,294,434,289,467,164,549,749,617,983,925,751,418,762,588,175,303,673,320,469,455,249,515,9,285,636,944,428,243,532,308,731,636,211,609,791]
# output
output = sol.bestRotation(nums)
# answer
answer = 146
print(output, answer, answer == output)