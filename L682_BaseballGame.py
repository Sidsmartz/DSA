class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L=[]
        for i in operations:
            if i=="D":
                L.append(int(L[-1]*2))
            elif i=='+':
                L.append(int(L[-1]+L[-2]))
            elif i=="C":
                L.pop()
            else:
                L.append(int(i))

        return sum(L)
    
#Basic Stack operations
    
#O(n) time complexity
#O(n) space complexity
