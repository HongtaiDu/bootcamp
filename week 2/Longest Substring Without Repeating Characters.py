class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        arr = {}
        maxLength = 0
        for r in range(len(s)):
            if s[r] in arr:
                if arr[s[r]]+1>l: 
                    l = arr[s[r]]+1
            arr[s[r]] = r 
            maxLength = max(maxLength, r-l+1)
        return maxLength