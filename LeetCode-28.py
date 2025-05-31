class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        
        n, m = len(needle), len(haystack)
        hay = haystack[0:n]
