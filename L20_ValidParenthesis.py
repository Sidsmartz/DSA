class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    p = stack.pop()
                    #Latest stack element popped to see if it matches
                    if(p != map[c]):
                        return False
        return not stack       
                

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

#Input: s = "()"
#Output: true

#Input: s = "()[]{}"
#Output: true

#O(n) time complexity
#O(n) space complexity



