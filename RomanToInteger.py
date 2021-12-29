"""
Problem 13 : Roman numerals are represented by seven different
             symbols: I, V, X, L, C, D and M. Convert Roman to Integer.
 
"""

class Solution:
    def romanToInt(self, s):
        d={
            "I":1,"V":5,"X":10,"L":50,"C":100,"M":1000,"D":500
        }
        res=0
        i=len(s)-1
        while(i>0):
            if s[i]=="V" and s[i-1]=="I":
                res+=4
                i-=2
            elif s[i]=="X" and s[i-1]=="I":
                res+=9
                i-=2
            elif s[i]=="L" and s[i-1]=="X":
                res+=40
                i-=2
            elif s[i]=="C" and s[i-1]=="X":
                res+=90
                i-=2
            elif s[i]=="D" and s[i-1]=="C":
                res+=400
                i-=2
            elif s[i]=="M" and s[i-1]=="C":
                res+=900
                i-=2
            else:
                res+=d[s[i]]
                i-=1
        if i==0:
            # print(i,s[i])
            res+=d[s[i]]
        
        return res
