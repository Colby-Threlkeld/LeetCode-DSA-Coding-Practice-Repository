'''
Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Problem: LeetCode 111: Minimum Depth of Binary Tree (Best Time: 5:32)

Time Complexity: O(n), Space Complexity: O(h) ... Recursion stack (h = height of the tree)
'''

#defining tree node class
class TreeNode(object):
  def __init__ (self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def minDepth(self, root):
    if not root: #if there is no child node, return 0
      return 0

    #if either the left or right has no child nodes return 1 + the opposite side
    if not root.left:
      return 1 + self.minDepth(root.right)
    if not root.right:
      return 1 + self.minDepth(root.left)
  
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) #Lastly, return 1 + the minimum of the deepest child node from left & right
