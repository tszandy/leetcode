from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line_char_count = 0
        line_char_count_except_space = 0
        line_list = []
        
        return_list = []
        for word in words:
            if line_list and line_char_count+len(word)+1>maxWidth:
                return_list.append(self.format_string(line_list,line_char_count_except_space,maxWidth))
                line_char_count = 0
                line_char_count_except_space = 0
                line_list = []
            line_list.append(word)
            line_char_count_except_space+=len(word)
            line_char_count+=len(word)
            if len(line_list)!=1:
                line_char_count+=1
        return_list.append(self.last_line_format_string(line_list,line_char_count_except_space,maxWidth))
        return return_list
                
            
    def format_string(self,line_list: List[str],line_char_count_except_space: int, max_width: int):
        space_count = max_width - line_char_count_except_space
        word_count = len(line_list)
        gap = word_count-1
        return_string = ""
        if len(line_list)==1:
            return_string += line_list[0]+" "*space_count
        else:
            for word in line_list[:-1]:
                return_string += word+" "*ceil(space_count/gap)
                space_count -= ceil(space_count/gap)
                gap -=1
            return_string +=line_list[-1]

        return return_string
    
    def last_line_format_string(self,line_list: List[str],line_char_count_except_space: int, max_width: int):
        space_count = max_width - line_char_count_except_space
        word_count = len(line_list)
        return_string = ""
        for word in line_list:
            if space_count:
                return_string += word+" "
                space_count -= 1
            else:
                return_string += word
        return_string +=" "*space_count
        return return_string


sol = Solution()

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

print(sol.fullJustify(words,maxWidth))