class Solution(object):
    def romanToInt(self, s):
       dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
       number = 0
       for i in range(len(s)):
         if i < (len(s)-1) and  dictionary[s[i]] < dictionary[s[i+1]]:
            number-=dictionary[s[i]]
         else:    
           number +=dictionary[s[i]]
       return number  