#268. Missing Number
#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        
        for i in range(n):
            sum+=nums[i]
        
        rangesum = n*(n+1)/2
        missing = rangesum-sum
        return int(missing)