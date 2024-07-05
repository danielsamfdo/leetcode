# https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftLeaves = []
        getLeftLeaves(root, leftLeaves)
        return sum([x.val for x in leftLeaves])
    
def getLeftLeaves(root: Optional[TreeNode], leftLeaves : List[TreeNode]):
    if root:
        if root.left:
            x = root.left
            if x.left == None and x.right == None:
                leftLeaves.append(x)
            getLeftLeaves(root.left, leftLeaves)
        if root.right:
            getLeftLeaves(root.right, leftLeaves)
