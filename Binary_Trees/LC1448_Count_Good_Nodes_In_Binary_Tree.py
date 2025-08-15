# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def goodNodes(self, root: TreeNode) -> int:  
        if not root: # if tree is empty return 0
            return 0
      
        def dfs(node, curMax):
            if not node: # if no child node exists return 0
                return 0
            # checking for "good" nodes
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
          
        count = [0] # mutable counter list for counting "good" nodes
        dfs(root, root.val) # calls recursive function

        return count[0] # return count val 
'''
time: O(n), Space: O(h) -> h = height of tree
'''
