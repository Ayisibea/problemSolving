class Solution:
    def findMaxAverage(self, nums, k):
        currentSum = sum(nums[:k])
        maxSum = currentSum
        for i in range(len(nums)-k):
            currentSum -=nums[i]
            currentSum += nums[i+k]

            maxSum =max(maxSum, currentSum)
        return maxSum/k    
        