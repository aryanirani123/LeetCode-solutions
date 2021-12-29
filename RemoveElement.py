"""
Problem 27 : Given an integer array nums and an integer val, 
             remove all occurrences of val in nums in-place. 
             The relative order of the elements may be changed
"""

class Solution(object):
    def removeElement(self, nums, val):
        length = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1

        return length

