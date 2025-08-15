'''
decimal        binary
integer        integer
–––––––        –––––––
1                 1
4               100
16             10000
64           1000000
256         100000000 
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        return  n.bit_length()%2 == 1 and n.bit_count() == 1
