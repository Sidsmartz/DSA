class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        # Also numbers ending in 0 (but not 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        # For even length numbers: x == reverted
        # For odd length: x == reverted // 10 (middle digit doesn't matter)
        return x == reverted or x == reverted // 10
