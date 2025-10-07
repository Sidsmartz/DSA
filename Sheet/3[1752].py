#1752. Check if Array Is Sorted and Rotated
#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

#There may be duplicates in the original array.

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count+=1
        
        return count<=1
        