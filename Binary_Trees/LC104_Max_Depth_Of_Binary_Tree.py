'''
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

Problem: LeetCode 104: Maximum Depth of Binary Tree (Best Time: 4:32)

Time Complexity: O(n), Space Complexity: O(h) ... (h = height of the tree)
'''

#defining binary tree node
class TreeNode(object):
  def __init__ (self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def maxDepth(self, root):
    if not root:
      return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # return 1 + the max of the deepest left node and deepest right node
