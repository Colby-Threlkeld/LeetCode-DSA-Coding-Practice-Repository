class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #empty set for storing seen values
        l = 0 #declaring left pointer
        res = 0 #declaring base result value

        #for loop to create right pointer and iterate string
        for r in range(len(s)):
            while s[r] in charSet: #while there is a duplicate char in set
                charSet.remove(s[l]) #remove leftmost character
                l += 1 #increment l forward by 1

            charSet.add(s[r]) #adds r values to set
            res = max(res, r - l + 1) #takes the base result, or current window size

        return res


'''
time: O(n)

"Sliding Window" technique
'''
