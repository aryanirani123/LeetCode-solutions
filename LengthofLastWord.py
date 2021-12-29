"""
Problem 58 : Given a string s consisting of some words separated 
             by some number of spaces, return the length of the 
             last word in the string.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="" :
            return 0

        split_list=s.split()
        print(split_list)
        if len(split_list)==0:
            return 0
        last_word=split_list[-1]
        print(last_word)
        return len(last_word)
        
        """"
        print(str(s))
        #print(s.split(" "))
        lis = list(s.split(" "))
        #print(len(lis[-1]))
        return len(lis[-1])
"""
