class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for i in nums:
            if count == 0:
                ans = i
            
            if(i == ans):
                count+=1
            else:
                count-=1
        
        return ans

        #Time Complexity: O(n)
        #Space Complexity: O(1)

        #Better than O(n), O(n) solution to store counts in hashmap