'''
Link: https://leetcode.com/problems/diameter-of-binary-tree/description/?envType=problem-list-v2&envId=plakya4j

Problem: LeetCode 543 Diameter of Binary Tree (Best Time: )

Time Complexity: Space Complexity: 
'''
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0 

        def dfs(node):
            if not node:
                return 0
        
            left = dfs(node.left) # length of left
            right = dfs(node.right) # length of right

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return self.diameter 


      
