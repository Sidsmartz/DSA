#189. Rotate Attay 
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        #In case k>len(nums)

        #nums[:] = nums[-k:] + nums[:-k] Python Slicing Solution

        def reverse(nums, left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

        reverse(nums,0,n-1)
        #Whole array reversal

        reverse(nums,0,k-1)
        #Reverses the first k elements

        reverse(nums,k,n-1)

        return nums