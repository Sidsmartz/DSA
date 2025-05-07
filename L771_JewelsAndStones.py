class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        h = set(jewels)
        count = 0

        for i in stones:
            if i in h:
                count+=1
            else:
                continue
        
        return count
    
#Time Complexity: O(n+m)
#Space Complexity: O(n)

#Makes a set of jewels and then iterates through stones to count how many are in the set

#Better than O(n*m) solution where stones iterate and check jewels as string
#as hash lookup is O(1), time complexity is O(n+m)

