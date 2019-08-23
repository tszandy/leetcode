import unittest
from onq4_Median_of_Two_Sorted_Arrays import Solution
sol = Solution()
class TestMedianSortedArray(unittest.TestCase):
    def test_case1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(2.0 ,sol.findMedianSortedArrays(nums1,nums2))

    def test_case2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(2.5 ,sol.findMedianSortedArrays(nums1,nums2))

    def test_case3(self):
        nums1 = [1, 4]
        nums2 = [2, 3]
        self.assertEqual(2.5,sol.findMedianSortedArrays(nums1,nums2))

if __name__ == '__main__':
    unittest.main()
