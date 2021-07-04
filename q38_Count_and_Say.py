from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def countAndSay(self, n: int) -> str:
        count_digit = 1
        return_string = "1"
        if n == 1:
            return return_string
        
        while n != count_digit:
            val = -1
            count = 0
            next_string = ""
            for char in return_string:
                if val != char and count !=0:
                    next_string+=str(count)+val
                    val = char
                    count = 1
                elif val != char:
                    val = char
                    count = 1
                else:
                    count+=1
            if count !=0:
                next_string+=str(count)+char
            return_string = next_string
            count_digit += 1
        return return_string

sol = Solution()


# input
n = 1
# output
output = sol.countAndSay(n)
# answer
answer = "1"
print(output, answer, answer == output)

# input
n = 4
# output
output = sol.countAndSay(n)
# answer
answer = "1211"
print(output, answer, answer == output)

# input
n = 26
# output
output = sol.countAndSay(n)
# answer
answer = "1113122113121113222123211211131211121311121321123113213221121113122123211211131221121311121312211213211321322112311311222113311213212322211211131221131211221321123113213221121113122113121113222112131112131221121321131211132221121321132132211331121321232221123113112221131112311322311211131122211213211331121321122112133221121113122113121113222123211211131211121311121321123113111231131122112213211321322113311213212322211231131122211311123113223112111311222112132113311213211221121332211231131122211311123113321112131221123113111231121113311211131221121321131211132221123113112211121312211231131122113221122112133221121113122113121113222123211211131211121311121321123113213221121113122113121113222113221113122113121113222112132113213221232112111312111213322112311311222113111221221113122112132113121113222112311311222113111221132221231221132221222112112322211213211321322113311213212312311211131122211213211331121321123123211231131122211211131221131112311332211213211321223112111311222112132113213221123123211231132132211231131122211311123113322112111312211312111322111213122112311311123112112322211213211321322113312211223113112221121113122113111231133221121321132132211331121321232221123123211231132132211231131122211331121321232221123113112221131112311332111213122112311311123112112322211211131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112211322212322211231131122211322111312211312111322211213211321322113311213211331121113122122211211132213211231131122212322211331222113112211"
print(output, answer, answer == output)
