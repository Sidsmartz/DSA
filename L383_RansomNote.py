class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -=1

        return True

#Time: O(n*m)
#Space: O(1)
#Not O(m) as only alphabets lowercase considered, max keys = 26 no matter
#how long dictionary is