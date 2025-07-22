class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        count = -1

        for num in s:
            curr = num
            length = 1
            while curr*curr in s:
                curr*=curr
                length+=1
            if length>1:
                count=max(count, length)
        
        return count

#Store everything in a set
#Update the iterator to check whether next square is in the set
#O(n) Time and Space [Time technically O(n * log log max_val)]