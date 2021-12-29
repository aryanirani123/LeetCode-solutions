"""
Problem 35 : Given a sorted array of distinct integers and a target value, 
             return the index if the target is found. If not, return the 
             index where it would be if it were inserted in order.

"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        print(nums)
        print(target)
        
        
        if target in nums:
            return nums.index(target)
        
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
            
        
