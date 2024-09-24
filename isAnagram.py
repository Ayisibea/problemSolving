class Solution(object):
    def isAnagram(self, s, t):
        count1 = {}
        count2 = {}
        for i in s:
            if i in count1:
                count1[i] +=1
            else:
                count1[i]= 1
        for j in t:
            if j in count2:
                count2[j] +=1
            else:
                count2[j]= 1    
        if count1 == count2:
            return True
        else:
            return False    