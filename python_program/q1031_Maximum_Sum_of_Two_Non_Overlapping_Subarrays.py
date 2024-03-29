from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def dp (l,r,sub_len):
            if r-l+1==sub_len:
                return sum(nums[l:r+1])
            max_sub = 0
            for i in range(l+sub_len-1,r+1):
                max_sub = max(max_sub,dp(i-sub_len+1,i,sub_len))
            return max_sub
        
        def max_sum_two_no_overlap(l,r,firstLen,secondLen):
            max_sub = 0
            
            for i in range(firstLen,n-secondLen+1):
                left_sum = dp(0,i-1,firstLen)
                right_sum = dp(i,n-1,secondLen)
                max_sub = max(max_sub,left_sum+right_sum)
 
            for i in range(secondLen,n-firstLen+1):
                left_sum = dp(0,i-1,secondLen)
                right_sum = dp(i,n-1,firstLen)
                max_sub = max(max_sub,left_sum+right_sum)
            return max_sub
        return max_sum_two_no_overlap(0,n-1,firstLen,secondLen)

sol = Solution()


# input
nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2
# output
output = sol.maxSumTwoNoOverlap(nums,firstLen,secondLen)
# answer
answer = 20
print(output, answer, answer == output)

# input
nums = [3,8,1,3,2,1,8,9,0]
firstLen = 3
secondLen = 2
# output
output = sol.maxSumTwoNoOverlap(nums,firstLen,secondLen)
# answer
answer = 29
print(output, answer, answer == output)

# input
nums = [802, 597, 447, 710, 76, 703, 384, 201, 2, 149, 506, 669, 898, 647, 864, 845, 545, 808, 375, 639, 520, 378, 897, 183, 894, 673, 842, 992, 520, 204, 375, 215, 697, 440, 189, 250, 9, 602, 45, 314, 952, 124, 557, 940, 711, 478, 827, 398, 852, 241, 123, 112, 28, 721, 120, 840, 953, 875, 221, 83, 704, 56, 224, 707, 176, 710, 980, 694, 277, 365, 513, 913, 9, 924, 675, 409, 794, 124, 825, 942, 857, 341, 259, 345, 300, 891, 568, 400, 832, 198, 124, 357, 643, 633, 493, 218, 539, 692, 691, 211, 139, 228, 577, 761, 173, 176, 195, 380, 363, 203, 472, 177, 313, 935, 930, 601, 882, 995, 986, 623, 272, 334, 479, 184, 363, 347, 501, 300, 404, 611, 216, 232, 525, 60, 397, 418, 408, 650, 446, 63, 495, 676, 368, 181, 932, 476, 430, 680, 468, 898, 802, 519, 419, 535, 802, 237, 616, 23, 580, 541, 612, 26, 981, 509, 969, 532, 306, 527, 928, 274, 878, 691, 490, 560, 800, 951, 675, 790, 122, 291, 972, 118, 646, 401, 543, 583, 43, 869, 878, 279, 552, 238, 764, 244, 32, 715, 974, 732, 424, 728, 477, 285, 170, 167, 623, 483, 775, 374, 806, 365, 561, 566, 208, 761, 45, 770, 852, 640, 344, 24, 162, 331, 451, 946, 70, 788, 855, 39, 764, 869, 424, 142, 124, 191, 565, 355, 758, 887, 651, 858, 382, 811, 937, 192, 594, 604, 666, 756, 702, 633, 787, 855, 974, 49, 748, 986, 936, 899, 104, 631, 45, 316, 444, 484, 100, 350, 859, 382, 187, 188, 361, 702, 159, 692, 712, 596, 242, 368, 944, 627, 363, 309, 103, 640, 544, 338, 522, 263, 202, 390, 883, 765, 664, 391, 209, 543, 352, 794, 894, 837, 918, 103, 198, 539, 240, 533, 52, 903, 878, 958, 711, 917, 725, 423, 425, 825, 401, 287, 660, 10, 802, 765, 647, 321, 339, 833, 800, 472, 263, 650, 529, 34, 897, 374, 521, 489, 636, 449, 985, 449, 281, 70, 61, 547, 912, 681, 949, 330, 423, 855, 873, 281, 832, 282, 63, 939, 29, 917, 734, 126, 520, 802, 939, 656, 288, 562, 913, 4, 279, 251, 104, 432, 603, 487, 131, 810, 726, 579, 832, 613, 174, 641, 978, 979, 950, 300, 96, 262, 208, 348, 833, 676, 163, 465, 575, 539, 924, 496, 329, 227, 979, 60, 542, 108, 457, 743, 719, 215, 47, 345, 228, 422, 429, 381, 305, 402, 205, 627, 414, 953, 453, 372, 857, 299, 485, 100, 433, 637, 377, 561, 596, 900, 577, 687, 738, 264, 179, 250, 604, 417, 457, 86, 691, 144, 45, 670, 629, 838, 212, 343, 862, 904, 315, 945, 147, 804, 693, 564, 655, 961, 333, 264, 269, 735, 384, 83, 685, 534, 31, 300, 30, 454, 438, 207, 74, 16, 95, 234, 344, 464, 134, 178, 450, 590, 6, 43, 641, 47, 129, 143, 833, 428, 989, 594, 917, 568, 415, 177, 795, 101, 185, 564, 16, 215, 238, 609, 917, 577, 148, 884, 198, 795, 845, 476, 62, 621, 725, 691, 537, 402, 855, 540, 379, 278, 671, 512, 143, 229, 187, 181, 644, 9, 208, 787, 32, 301, 697, 565, 755, 667, 323, 388, 235, 258, 146, 961, 997, 446, 951, 860, 931, 30, 599, 64, 417, 203, 7, 273, 504, 588, 321, 895, 953, 786, 839, 603, 821, 293, 300, 360, 304, 112, 190, 317, 957, 574, 627, 636, 960, 993, 434, 797, 966, 705, 357, 380, 857, 765, 244, 806, 468, 219, 597, 793, 44, 810, 863, 83, 60, 592, 509, 609, 970, 10, 306, 116, 382, 500, 361, 18, 798, 375, 856, 757, 37, 459, 691, 79, 807, 544, 277, 910, 930, 429, 153, 235, 650, 392, 73, 104, 678, 216, 382, 348, 963, 248, 89, 736, 595, 431, 243, 656, 424, 598, 521, 463, 888, 702, 720, 725, 616, 935, 978, 513, 757, 977, 657, 343, 290, 447, 654, 819, 219, 539, 669, 25, 5, 981, 187, 655, 988, 266, 798, 326, 641, 482, 705, 775, 329, 385, 280, 571, 700, 135, 495, 850, 71, 832, 523, 88, 430, 596, 166, 132, 869, 615, 591, 973, 344, 679, 328, 480, 688, 883, 925, 403, 125, 63, 162, 867, 233, 363, 745, 614, 208, 51, 528, 748, 529, 500, 248, 865, 59, 541, 950, 922, 881, 151, 225, 969, 693, 417, 630, 82, 762, 628, 746, 426, 521, 449, 361, 41, 381, 105, 241, 843, 394, 57, 326, 787, 507, 945, 898, 907, 435, 901, 136, 216, 290, 87, 923, 175, 309, 591, 255, 509, 403, 562, 431, 918, 508, 428, 454, 524, 424, 864, 65, 825, 841, 289, 281, 397, 516, 92, 477, 927, 686, 440, 235, 509, 940, 965, 100, 282, 922, 243, 53, 330, 491, 571, 374, 95, 37, 918, 671, 348, 846, 136, 913, 629, 766, 916, 988, 196, 381, 356, 524, 425, 226, 817, 41, 275, 669, 325, 924, 901, 31, 612, 96, 684, 92, 663, 130, 953, 999, 912, 629, 757, 484, 848, 20, 817, 5, 185, 742, 94, 846, 318, 976, 977, 172, 273, 310, 444, 161, 655, 820, 155, 251, 414, 873, 197, 807, 563, 489, 737, 198, 858, 568, 162, 499, 395, 826, 830, 55, 358, 372, 776, 57, 442, 945, 792, 144, 796, 572, 819, 173, 946, 994, 82, 733, 554, 807, 205, 9, 134, 521, 743, 474, 225, 3, 242, 465, 264, 982, 991, 361, 759, 268, 450, 793, 820, 977, 569, 270, 346, 371, 600, 874, 223, 219, 359, 29, 776, 678, 62, 550, 168, 844, 180, 23, 787, 310, 943, 705, 966, 472, 768, 603, 650, 160, 109, 926, 442, 513, 214, 880, 423, 967, 34, 135, 493, 191, 497, 354, 416, 672, 260, 776, 811, 658, 135, 485, 979, 418, 159, 614, 46, 744, 179, 385, 852, 280, 760, 662, 150, 738, 232, 649, 771, 578, 625, 766, 399, 658, 640, 929, 882, 547, 751, 317, 275, 982, 887, 415, 549, 581, 367, 517, 183]
firstLen = 50
secondLen = 30
# output
output = sol.maxSumTwoNoOverlap(nums,firstLen,secondLen)
# answer
answer = 47392
print(output, answer, answer == output)
