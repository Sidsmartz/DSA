class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'

        for c in text:
            if c in balloon:
                counter[c]+=1
            
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])

        #Goes through the given text and counts instances of letters required
        #Minimum no. of times word is formed is given

        #Time Complexity: O(n)
        #Space Complexity: O(1) As only b,a,l,o,n characters are stored