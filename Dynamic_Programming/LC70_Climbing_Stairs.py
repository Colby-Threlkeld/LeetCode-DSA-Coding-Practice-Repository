# Link: https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=plakya4j
# Problem: Climbing Stairs (Best Time: 30:34)


# **Fibonacci style problem**
class Solution(object):
    def climbStairs(self, n):
        #base cases
        if n == 1: 
            return 1
        if n ==2:
            return 2

        one = 1
        two = 2

        for i in range(3, n+1):
            current = one + two
            one = two #moves window forward
            two = current #two holds latest result

        return two
