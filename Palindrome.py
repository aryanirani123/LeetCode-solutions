class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        og_num=0
        while(x>0):
            pos=x%10
            og_num=og_num*10+pos
            x=x//10
        if(temp==og_num):
            return True
