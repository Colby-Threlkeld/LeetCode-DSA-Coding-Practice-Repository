'''
Link: https://leetcode.com/problems/remove-element/description/

Problem: LeetCode 27: Remove Element
'''

class Solution(object):
    def removeElement(self, nums, val):
        j = 0 #write pointer
       
        for i in range(len(nums)): #read pointer
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j
