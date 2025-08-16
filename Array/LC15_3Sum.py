class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort() #sort list for two pointer approach

        for i, a in enumerate(nums): #i = index, a = value @ index
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #move pointer left to decrease sum when > 0
                    r -= 1
                elif threeSum < 0: #moves value right to increase sum when < 0
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) #if the triplets=target, append to list
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

'''
time: O(n^2)
'''
