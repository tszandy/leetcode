from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = dict(knowledge)
        
        result = ""
        for phrase in s.split("("):
            if ")" in phrase:
                phrase_list = phrase.split(")")
                need_replace_phrase = phrase_list[0]
                if need_replace_phrase in knowledge_dict:                
                    result += knowledge_dict[phrase_list[0]]+phrase_list[1]
                else:
                    result += "?"+phrase_list[1]                    
            else:
                result += phrase
        return result

sol = Solution()

s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(sol.evaluate(s,knowledge),"bobistwoyearsold","bobistwoyearsold"==sol.evaluate(s,knowledge))

s = "hi(name)"
knowledge = [["a","b"]]
print(sol.evaluate(s,knowledge),"hi?","hi?"==sol.evaluate(s,knowledge))

s = "(a)(a)(a)aaa"
knowledge = [["a","yes"]]
print(sol.evaluate(s,knowledge),"yesyesyesaaa","yesyesyesaaa"==sol.evaluate(s,knowledge))

s = "(a)(b)"
knowledge = [["a","b"],["b","a"]]
print(sol.evaluate(s,knowledge),"ba","ba"==sol.evaluate(s,knowledge))

