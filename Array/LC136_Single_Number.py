'''
| IMPORTANT! |
a ^ a = 0 (any number XOR itself is zero)

a ^ 0 = a (any number XOR zero is itself)

XOR is commutative and associative (order doesn’t matter)

So, if you XOR all numbers together:

All the numbers that appear twice will cancel out (become 0)

The single number will remain.

| EXAMPLE(bit manipulation): |

nums = [4, 1, 2, 1, 2]

We start with result = 0:

result = 0 ^ 4 = 4

result = 4 ^ 1 = 5 (binary: 100 ^ 001 = 101)

result = 5 ^ 2 = 7 (binary: 101 ^ 010 = 111)

result = 7 ^ 1 = 6 (binary: 111 ^ 001 = 110)

result = 6 ^ 2 = 4 (binary: 110 ^ 010 = 100) ✅

Final result = 4 — the single number.
'''
# WITH bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR
        return result

# WITHOUT bit manipulation (Worse)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()
