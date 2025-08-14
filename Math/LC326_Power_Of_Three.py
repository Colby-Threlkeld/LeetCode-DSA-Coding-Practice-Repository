class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False #no 3^k exists for these n
        while n % 3 == 0:
            n //= 3
        return n == 1 
