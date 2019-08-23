class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        if len(s)<=1:
            return len(s)

        count = 1
        record_set = set(s[0])
        for i in range(1,len(s)):
            if s[i] in record_set:
                break
            record_set.add(s[i])
            count+=1

        return max(count,self.lengthOfLongestSubstringList(1,s))

    def lengthOfLongestSubstringList(self,startindex,s):
        if len(s)-startindex<=1:
            return len(s)-startindex

        count = 1
        record_set = set(s[startindex])
        for i in range(startindex+1,len(s)):
            if s[i] in record_set:
                break
            record_set.add(s[i])
            count+=1

        return max(count,self.lengthOfLongestSubstringList(startindex+1,s))
