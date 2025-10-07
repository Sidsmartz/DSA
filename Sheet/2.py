#Second Largest Element
#Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

class Solution:
    def secondLargestElement(self, nums):
        second = largest = -float('inf')

        for i in nums:
            if i > largest:
                second = largest
                largest = i      
            elif i < largest and i > second:
                second = i  

        if second > -float('inf'):
            return second
        else:
            return -1