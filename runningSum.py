class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        Sum = 0
        for i in nums:
            Sum += i
            runningSum.append(Sum)
        return runningSum    
        