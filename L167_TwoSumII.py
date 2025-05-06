class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if(sum == target):
                return [l+1,r+1]
            elif(sum > target):
                r-=1
            else:
                l+=1
            
#Two pointers to find sum based on target value


#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

#O(n) time complexity
#O(1) space complexity


