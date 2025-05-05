class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        j = len(nums) - 1
        #Two pointers, left and right
        while i <= j:
            if(abs(nums[i]) > abs(nums[j])):
                #bigger number bigger square
                ans.append(nums[i]**2)
                i+=1
            else:
                ans.append(nums[j]**2)
                j-=1
        print(ans)
        return ans[::-1]


#Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

#Instead of O(nlogn) for sorting, this does O(n)
