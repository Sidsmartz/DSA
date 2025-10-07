#Union of two sorted arrays
#Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.
#The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

class Solution:
    def unionArray(self, nums1, nums2):
        return list(set(nums1)|set(nums2))
