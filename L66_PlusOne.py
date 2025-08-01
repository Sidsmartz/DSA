class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) - 1 

        for i in range(l,-1,-1):
            if(digits[i])<9:
                digits[i]+=1
                return digits

            #If number is 9, continue loop (carry)

            digits[i] = 0
        return [1] + digits

        return digits

#Time Complexity: O(n)
#Space Complexity: Best: O(1) Worst: O(n)