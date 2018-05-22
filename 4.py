# -*- coding: utf-8 -*-
#4
#算法

#给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
#请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
#示例 1:
#nums1 = [1, 3]
#nums2 = [2]
#中位数是 2.0
#示例 2:
#nums1 = [1, 2]
#nums2 = [3, 4]
#中位数是 (2 + 3)/2 = 2.5
import sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        L1 = L2 = R1 = R2 = c1 = c2 = lo = 0
        hi = 2*len1
        while lo <= hi:
            c1 = (lo + hi) // 2
            c2 = len1 + len2 -c1
            L1 = -sys.maxsize if (c1==0) else nums1[(c1-1)//2]
            R1 = sys.maxsize if (c1==2*len1) else nums1[c1//2]
            L2 = -sys.maxsize if (c2==0) else nums2[(c2-1)//2]
            R2 = sys.maxsize if (c2==2*len1) else nums2[c2//2]

            if L1 > R2:
                hi = c1 - 1
            elif L2 > R1:
                lo = c1 + 1
            else:
                break
        return (max(L1,L2)+ min(R1,R2))/2

solution = Solution()
result = solution.findMedianSortedArrays([],[1])
print(result)
