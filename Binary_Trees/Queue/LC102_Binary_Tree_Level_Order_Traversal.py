# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        #create queue and initially add the root of tree
        q = collections.deque()
        q.append(root)

        #while there is a value in the queue
        while q:
            qLen = len(q) #stores queue len
            level = [] #empty list for level-by-level storage

            for i in range(qLen):
                node =  q.popleft() #store left most node
                if node:
                    level.append(node.val) #if node has a vlue append it to the level
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level) #if level contains elements append to the res list

        return res

  '''
  time: O(n)
  '''
