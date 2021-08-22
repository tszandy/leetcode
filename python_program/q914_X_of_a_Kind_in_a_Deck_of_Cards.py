from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<2:
            return False
        deck_counter = Counter(deck)
        if len(deck_counter.keys())==1:
            return True
        distinct_card = list(deck_counter.keys())
        total_gcd = gcd(deck_counter[distinct_card[0]],deck_counter[distinct_card[1]])
        if total_gcd == 1:
            return False
        for i in range(2,len(distinct_card)):
            total_gcd = gcd(total_gcd, deck_counter[distinct_card[i]])
            if total_gcd == 1:
                return False
        return True
sol = Solution()

print(sol.hasGroupsSizeX())