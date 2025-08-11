'''
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

Problem: LeetCode 26: Removing Duplicates From a Sorted Array (Best Time: 14:32)
'''
class Solution(object):
    def removeDuplicates(self, nums):
        #check for empty list first
        if not nums:
            return 0

        insert_pos = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: #new unique number appears when i != 1-1
                nums[insert_pos] = nums[i] #write in place at the next position
                insert_pos += 1 #increment unique prefix

        return insert_pos

       
