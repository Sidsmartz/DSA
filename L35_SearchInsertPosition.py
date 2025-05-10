class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l<=r:
            middle = (l+r)//2

            if (nums[middle]) < target:
                l = middle + 1
            elif (nums[middle] > target):
                r = middle - 1
            else:
                return middle

        if(nums[middle]<target):
            return middle+1
        else:
            return middle
            #Sorted so higher number in front of current number

        #Time Complexity: O(log n)
        #Space Complexity: O(1)
