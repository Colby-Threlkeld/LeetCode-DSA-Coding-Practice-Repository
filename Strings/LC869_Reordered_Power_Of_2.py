'''
Link: https://leetcode.com/problems/reordered-power-of-2/description/

Problem: Daily Problem, LeetCode 869: Reordered Power Of 2 (Medium )

Time Complexity: O(1), Space Complexity: O(1)
'''
class Solution:
  def reorderedPowerOf2(self, n):
    sig = sorted(str(n)) #converts number into a string of individual digits

    for k in range(31): #in range 31, so that we only test within constraint 1e^9
      if sorted(str(2**k)) == sig: #if sorted string of digits == a power of two, then return True
        return True

    return False #Else: False
         
