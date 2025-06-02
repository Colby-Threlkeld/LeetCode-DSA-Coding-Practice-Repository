# Link: https://leetcode.com/problems/palindrome-number/description/
# Problem 9: Palindrome Number 


class Solution:
    def isPalindrome(self, x):
        initial = str(x)

        reverse = initial[::-1]

        return initial == reverse
