class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        

    def sumRange(self, left, right):
        Sum = 0
        for i in self.nums[left:right+1]:
            Sum += i    
        return Sum