'''
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description

Problem: LeetCode 4: Median Of Two Sorted Arrays -> Hard level question
'''
class Solution:
    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        left_len = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = left_len - i

            Aleft  = A[i-1] if i > 0 else float('-inf')
            Aright = A[i]   if i < m else float('inf')
            Bleft  = B[j-1] if j > 0 else float('-inf')
            Bright = B[j]   if j < n else float('inf')

            if Aleft > Bright:
                high = i - 1
            elif Bleft > Aright:
                low = i + 1
            else:
                if (m + n) % 2:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
        
