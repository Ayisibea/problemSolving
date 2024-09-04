class Solution(object):
    def reverseString(self,s):
      result =[]  
      for i in range(len(s)-1,-1,-1):
        result+=s[i]
      return result 