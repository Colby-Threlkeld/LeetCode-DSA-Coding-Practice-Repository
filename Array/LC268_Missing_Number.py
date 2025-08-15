class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i]) #as i iterates through we subtract values from nums

        
        return res#after nums values are subtracted only the missing number is left

'''
time: O(n)
'''
