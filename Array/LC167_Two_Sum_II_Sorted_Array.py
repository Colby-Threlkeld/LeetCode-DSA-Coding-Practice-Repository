class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 #establish two pointers
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum < target: #if sum<target increase sum
                l += 1
            elif curSum > target: #if sum>target decrease sum
                r -= 1
            else:
                return [l+1, r+1] #ensures answer is 1 indexed, since python is 0

        return []


'''
time: O(n)
'''
