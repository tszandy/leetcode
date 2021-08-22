from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
            
        longest_palindrome = ""
        longest_palindrome_length = 0
        
        dp_list = []
        for i in range(len(s)):
            substring = s[i:i+1]
            if len(substring)>longest_palindrome_length:
                longest_palindrome=substring
                longest_palindrome_length = len(substring)
            dp_list.append((i,i))
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                substring = s[i:i+2]
                longest_palindrome=substring
                longest_palindrome_length = len(substring)
                dp_list.append((i,i+1))
        
        while dp_list:
            left_index,right_index = dp_list.pop(0)
            if left_index>0 and right_index<len(s)-1 and s[left_index-1]==s[right_index+1]:
                dp_list.append((left_index-1,right_index+1))
                substring = s[left_index-1:right_index+2]
                longest_palindrome=substring
                longest_palindrome_length = len(substring)

        return longest_palindrome

sol = Solution()

print(sol.longest_palindrome())

# test_set
s = "babad"
s = "cbbd"
s = "a"
s = "ac"
s = "ccc"