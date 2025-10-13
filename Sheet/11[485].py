#485. Max Consecutive Ones
#Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxlen = 0
        count = 0

        for i in range(len(nums)):
            if nums[i]:
                count+=1
                maxlen = max(maxlen, count)
            else:
                count = 0

        return maxlen