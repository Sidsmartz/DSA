#1800. Maximum Ascending Subarray Sum

#Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

#A subarray is defined as a contiguous sequence of numbers in an array.

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = nums[0]
        tempsum = nums[0]
        n = len(nums)
        for i in range(n-1):
            if(nums[i] < nums[i+1]):
                tempsum+=nums[i+1]
            else:
                maxsum = max(maxsum,tempsum)
                tempsum=nums[i+1]

        maxsum = max(maxsum,tempsum)
        return maxsum