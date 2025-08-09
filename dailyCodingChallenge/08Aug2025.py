class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

#Time Complexity: O(1)
#Space Complexity: O(1)