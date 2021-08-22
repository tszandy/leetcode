from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        length_binary_form_start = len(bin(start)[2:])
        binary_form_start = "0"*(n-len(bin(start)[2:]))+bin(start)[2:]
        permutation_list = []
        if binary_form_start[0] == "0":
            permutation_list.append("0")
            permutation_list.append("1")
        else:
            permutation_list.append("1")
            permutation_list.append("0")
            
        for c in binary_form_start[1:]:
            next_permutation_list = []
            current_label = c
            for permutation in permutation_list:
                if current_label == "0":
                    next_permutation_list.append(permutation+"0")
                    next_permutation_list.append(permutation+"1")
                    current_label = "1"
                else:
                    next_permutation_list.append(permutation+"1")
                    next_permutation_list.append(permutation+"0")
                    current_label = "0"
            permutation_list = next_permutation_list
        return list(map(lambda x:int(x,2),permutation_list))

sol = Solution()

print(sol.circularPermutation())