from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','').replace('-','+-').replace('--','-').replace('++','+')
        string_list = ['']
        count = 0
        for i in range(len(s)):
            # print(string_list)
            if s[i]=="(":
                string_list.append("")
                continue
            if s[i]==")":
                bracket_result = str(self.calculate_standard(string_list.pop()))
                string_list[-1] += bracket_result
                continue
            string_list[-1]+=s[i]
        return self.calculate_standard(string_list[0])

    def calculate_standard(self,s:str) -> int:
        s = s.replace("--","+")
        return sum(map(lambda x:int(x),filter(lambda x:len(x)!=0,s.split('+'))))
        

sol = Solution()

print(sol.calculate())