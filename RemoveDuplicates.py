"""
Problem 26: Given an integer array nums sorted in non-decreasing order, 
            remove the duplicates in-place such that each unique element 
            appears only once. The relative order of the elements should be kept the same.

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i<len(nums):
            if nums[i] != nums[i-1]:
                i = i+1
            else:
                nums.remove(nums[i-1])
