from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        last = [0] * 32  # For each bit (0 to 31), track the farthest index where it's needed

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if (nums[i] >> b) & 1:  # If bit 'b' is set in nums[i]
                    last[b] = i  # Update the last seen index for this bit

            # The farthest index we need to go to from i to include all bits needed
            max_idx = i
            for b in range(32):
                max_idx = max(max_idx, last[b])
            
            ans[i] = max_idx - i + 1  # Length of the smallest subarray

        return ans

#Time Complexity: O(n) (n*32 -> n*constant)
#Space Complexity: O(n) (n+32)