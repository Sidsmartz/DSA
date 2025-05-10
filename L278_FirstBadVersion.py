# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l<r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
                #Since first bad version needed, previous can be bad aswell
            else:
                l = m + 1

        return r

        #Time Complexity: O(log n)
        #Space Complexity: O(1)
        #Better than O(n) because we are using binary search instead
        #of going through each element/'version' and calling the API

