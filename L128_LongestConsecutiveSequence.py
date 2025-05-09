class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in s:
                next = i + 1
                length = 1
                
                while next in s:
                    length+=1
                    next+=1
                
                longest = max(longest,length)
                
        return longest