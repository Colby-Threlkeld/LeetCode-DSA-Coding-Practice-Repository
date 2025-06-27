# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Problem 28: Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        
        n, m = len(needle), len(haystack)
        hay = haystack[0:n]
