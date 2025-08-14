class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True: #finding the cycle to set up second loop
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:#send pointer from start because:Distance from start → cycle start
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow #return slow (or slow2) when they are both at the cycle start

            
