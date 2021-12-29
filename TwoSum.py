"""
Problem 1 : Given an array of integers nums and an integer target, 
            return indices of the two numbers such that they 
            add up to target.

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
 
