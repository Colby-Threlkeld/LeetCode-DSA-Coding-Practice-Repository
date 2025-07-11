'''
Link: https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=plakya4j

Problem:
'''

# brute force methods
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]
