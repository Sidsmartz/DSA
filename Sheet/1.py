#Largest Element

class Solution:
    def largestElement(self, nums):
        max = nums[0]
        for i in nums:
            if i > max:
                max = i
        
        return max