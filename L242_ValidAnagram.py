from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
    
#O(n) time complexity
#O(n) space complexity

#Makes frequency dictionaries of both strings and compares them
