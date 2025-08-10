class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sort_digits(num):
            return ''.join(sorted(str(num)))
        
        target = sort_digits(n)

        for i in range(31):  # 2^0 to 2^30 (2^30 < 10^9)
            power_of_2 = 1 << i  # Same as 2**i, but faster
            if sort_digits(power_of_2) == target:
                return True

        return False

#Time Complexity: O()
#Space Complexity: O(1)