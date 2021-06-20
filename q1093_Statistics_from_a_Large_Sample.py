from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        for i in range(len(count)):
            if count[i]!=0:
                minimum = i
                break

        for i in range(len(count))[::-1]:
            if count[i]!=0:
                maximum = i
                break

        mean = sum(map(lambda x:x[0]*x[1],enumerate(count)))/sum(count)
        
        sum_count = sum(count)
        # print(sum_count)
        half_sum_count = sum_count//2
        if sum_count%2==1:
            for i in range(len(count)):
                if half_sum_count-count[i]<0:
                    median = i
                    break
                half_sum_count-=count[i]

        else:
            first_median =""
            half_sum_count = sum_count//2
            for i in range(len(count)):
                if first_median !="" and count[i]:
                    median = (first_median + i)/2
                    break
                if first_median == "" and half_sum_count-count[i]<0:
                    median = i
                    break
                if first_median == "" and half_sum_count-count[i]==0:
                    first_median = i
                half_sum_count-=count[i]
        max_count = 0
        for i in range(len(count)):
            if max_count<count[i]:
                max_count = count[i]
                mode = i
        return minimum,maximum,mean,median,mode

sol = Solution()

print(sol.sampleStats())