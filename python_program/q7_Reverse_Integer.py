class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_x = str(abs(x))
        sign=x>=0
        return_int = 0
        for i in range(len(string_x))[::-1]:
            if string_x[i]==0 and return_int==0:
                continue
            else:
                return_int=return_int*10+int(string_x[i])
        return_int = return_int*(-1)**(1-sign)
        if return_int<=(2**31-1) and return_int>=-2**31:
            return return_int
        else:
            return 0
