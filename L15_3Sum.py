class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if nums[i]>0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
                #If same number, skip to remove duplicates

            l,h = i+1, n-1
            while l<h:
                summ = nums[i] + nums[l] + nums[h]
                if summ==0:
                    ans.append([nums[i],nums[l],nums[h]])
                    l,h = l+1,h-1
                    while l<h and nums[l] == nums[l-1]:
                        l+=1
                    while l<h and nums[h] == nums[h+1]:
                        h-=1
                elif summ < 0:
                    l+=1
                else:
                    h-=1
        return ans

        #Time Complexity: O(n^2)
        #Space Complexity: O(1) or O(n) based on sorting; in place or not