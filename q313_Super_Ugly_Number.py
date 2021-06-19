from heapq import *
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        final_list = [1]
        pq = [(primes[0],0)]
        while len(pq)!=0 and len(final_list)<n:            
            elem,index = heappop(pq)
            if elem not in final_list:
                final_list.append(int(elem))
            else:
                continue
            heappush(pq, (elem*primes[0],0))
            if index < len(primes)-1:
                heappush(pq, (elem/primes[index]*primes[index+1],index+1))
        return final_list[-1]
    
    def nthSuperUglyNumber_2(self, n: int, primes: List[int]) -> int:
        primes_list = np.array(primes)
        log_primes_list = np.log(primes_list)/np.log(primes_list[0]) 
        frequency_list = 1/log_primes_list
        portion_list = frequency_list / sum(frequency_list)
        max_count_list = np.ceil(portion_list*n)
        max_number = primes[-1]**(max_count_list[-1])
        print("max_count_list[-1]",max_count_list[-1])
        number_list = [1]
        print(max_number)
        return 0
        for i,prime in enumerate(primes):
            for number in number_list[:]:
                new_number = number
                while new_number < max_number:
                    new_number = new_number *prime
                    number_list.append(new_number)
        number_list = sorted(number_list)
        return number_list[n-1]


n = 10000
primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
a = Solution()
print(a.nthSuperUglyNumber(n,primes))