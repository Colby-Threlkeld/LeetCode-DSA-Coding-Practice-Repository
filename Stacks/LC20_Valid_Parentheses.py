'''
Link: https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=plakya4j

Problem: Problem 20: Valid Parentheses (Best Time: 17:45)

Time Complexity: O(n), Space Complexity: O(n)

'''

class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}

#If the char is an opening parentheses, append to stack for matching       
        for char in s:
            if char in matching.values():
                stack.append(char)

#If there's nothing in the stack, or if the last opened bracket doesn’t match the closing bracket we just saw, return False
            elif char in matching:
                if not stack or stack[-1] != matching[char]: 

                    return False

                stack.pop()

#If stack has a valid match return True, otherwise False
        return len(stack) == 0



                   
