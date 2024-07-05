# https://leetcode.com/problems/validate-binary-search-tree/editorial/
# is valid BST Check
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isNodeWithinRange(root, float('-inf'), float('inf'))

def isNodeWithinRange(root: Optional[TreeNode], leftMin: float, rightMax: float) -> bool:
    if root:
        if root.val > leftMin and root.val < rightMax:
            return isNodeWithinRange(root.left, leftMin, root.val) and isNodeWithinRange(root.right, root.val, rightMax)
        return False
    else:
        return True
