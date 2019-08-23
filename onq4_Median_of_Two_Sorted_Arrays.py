import bisect
import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m==0:
            return np.median(nums2)
        if n==0:
            return np.median(nums1)
        if m == 1 or n == 1:
            if m==1:
                a = n + 1
                bisect.insort(nums2,nums1[0])
                store_list = nums2
            else:
                a = m + 1
                bisect.insort(nums1,nums2[0])
                store_list = nums1
            if a % 2 == 1:
                return  store_list[int(a/2)]
            else:
                return np.mean(store_list[int(a/2-1):int(a/2+1)])

        halfmin = int(min(m,n)/2)
        if nums1[halfmin-1] < nums2[-halfmin]:
            return self.findMedianSortedArrays(nums1[halfmin:],nums2[:-halfmin])
        if nums1[-halfmin] > nums2[halfmin-1]:
            return self.findMedianSortedArrays(nums1[:-halfmin],nums2[halfmin:])
