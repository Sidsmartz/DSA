class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in nums:
            if(abs(i)) < abs(closest):
                closest = i
        if(closest<0 and abs(closest) in nums):
            #for -1, if 1 is in array return 1 since its larger
            return abs(closest)
        else:
            return closest



#Given an integer array nums of size n,
#return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.