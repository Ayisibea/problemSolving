class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        state = False
        for i in nums:
            if i in count:
                count[i] +=1
                state = True
            else:
                count[i]= 1
        return state