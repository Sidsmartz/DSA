class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num #target

        while l <= r:
            m = (l+r)//2
            if(m*m == num):
                return True
            elif(m*m < num):
                l = m + 1
            else:
                r = m - 1
        
        return False

        #Time Complexity: O(log n)
        #Space Complexity: O(1)
