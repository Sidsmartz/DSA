class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return [i,h[y]]
        
#Makes a hash map of nums and their indices
#Iterates through nums and checks if the complement of the current num
#is in the hash map and if its index is not the current index

#Time Complexity: O(n)
#Space Complexity: O(n)

