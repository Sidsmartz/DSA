class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        flag = 0
        while l<=r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue

            #If there's spaces or special characters, skip

            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                flag = 1
                return False
            
            #Two pointers to check if the characters are the same
        
        return True

#O(n) time complexity
#O(1) space complexity





