# Link: https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=plakya4j
# Problem 66: Plus One (Best Time: 16:24)

class Solution(object):
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):  # loop from right to left
            if digits[i] < 9:                   # if digit is less than 9
                digits[i] += 1                  # add 1
                return digits                   # return list
            digits[i] = 0                       # else, set to 0

        # special case if all digits were 9
        return [1] + [0] * len(digits)
