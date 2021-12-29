"""
Problem 88 : You are given two integer arrays nums1 and nums2,
             sorted in non-decreasing order, and two integers m and n, 
             representing the number of elements in nums1 and nums2 respectively.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=0
        for x in range(len(nums1)):
            if i>=n:
                break
            if nums1[x]==0:
                nums1[x]=nums2[i]
                i+=1           
        nums1.sort()
