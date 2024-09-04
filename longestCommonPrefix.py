class Solution(object):
    def longestCommonPrefix(self, strs):
         prefix=strs[0]
         for string in strs:
          if len(string)<len(prefix):
            prefix = string 
         for string in strs:
            j = 0
            while j<len(prefix) and string[j] == prefix[j]:
                j += 1
            prefix = prefix[:j]
         return prefix 