class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        n = len(s)
        i = 0
        sum = 0

        while (i<n):
            if(i < n-1 and d[s[i]] < d[s[i+1]]):
                #If right is higher than left, ex: IV = 4, subtract and skip both
                sum += d[s[i+1]] - d[s[i]]
                i+=2
            else:
                sum += d[s[i]] #else just add number
                i+=1

        return sum
    

#Time: O(n)
#Space: O(1)