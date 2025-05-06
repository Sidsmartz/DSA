class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for i in nums:
            if i in h:
                return True
            else:
                h.add(i)
                i+=1
        return False

#If number already in hashset, return true
#If not, add to hashset

#O(n) time complexity
#O(n) space complexity

