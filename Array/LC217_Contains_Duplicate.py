class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set() #using a set instead of a list for faster look up

    for i in nums:
      if i in seen:
        return True #if int is repeated, return True

      seen.add(i) #if int is new, add to set

    return False #if no int is repeated, return False
