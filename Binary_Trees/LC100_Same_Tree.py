'''
Link: https://leetcode.com/problems/same-tree/?envType=problem-list-v2&envId=plakya4j

Problem: LeetCode 100: Same Tree (Best Time: 14:32)

Time Complexity: O(n), Space Complexity: O(h) ... Recursion stack (h = height of the tree)
'''

# class for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: # if p and q are empty, they are the same
            return True

        if not p or not q: # if p or q (one or the other) are empty then they are different
            return False

        if p.val != q.val: # if p value does not = q value then they are different
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        
