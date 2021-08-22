from typing import List

class Solution:
    def originalDigits(self, s: str) -> str:
        count_char = Counter(s)
        digit_str = [("zero",0),("one",1),("two",2),("three",3),("four",4),("five",5),("six",6),("seven",7),("eight",8),("nine",9)]
        
        output_count = [0 for i in range(10)]
        keep_list = list(range(10))
        while keep_list:
            next_keep_list = []
            for i in keep_list:
                string, num = digit_str[i]
                char_counter = Counter(string)
                num_digits_in_str = min([count_char[key]//value for key,value in char_counter.items()])
                if num_digits_in_str>=1:
                    output_count[num]+=1
                    next_keep_list.append(i)
                    for key,value in char_counter.items():
                        count_char[key]-=value
            keep_list = next_keep_list
        
        output = ""
        for i,e in enumerate(output_count):
            output+=str(i)*e
        return output
            
        

sol = Solution()

print(sol.originalDigits())