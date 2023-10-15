class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        currentS = {}  
        currentT = {}
        newS = ""
        newT = ""
        firstS = "a"
        firstT = "a"
        for i in range(len(s)):
            if s[i] not in currentS:
                currentS[s[i]] = firstS #
                firstS = chr(ord(firstS)+1)
            newS += currentS[s[i]] 
            
            if t[i] not in currentT:
                currentT[t[i]] = firstT 
                firstT = chr(ord(firstT)+1)
            newT += currentT[t[i]] 
        return newS == newT