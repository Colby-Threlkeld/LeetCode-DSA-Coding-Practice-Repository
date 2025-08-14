class Solution:
  def largestGoodInteger(self, num: str) -> str:
    for d in "9876543210":
      t = d * 3

      if t in num:
        return t

    return ""
