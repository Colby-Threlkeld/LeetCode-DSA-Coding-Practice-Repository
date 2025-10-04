class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, max_count = 0,0

        for i in nums:
            count[i] = 1 + count.get(i, 0)
            res = i if count[i] > max_count else res
            max_count = max(count[i], max_count)
        return res
