# https://leetcode.com/problems/binary-tree-inorder-traversal/description/ 
# Binary Tree Inorder Traversal 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = []
        if root != None:
            iterative(root, solution)
        return solution

def recursive(root: Optional[TreeNode], solution: List[int]):
    if root.left:
        recursive(root.left, solution)
    solution.append(root.val)
    if root.right:
        recursive(root.right, solution)

def iterative(root: Optional[TreeNode], solution: List[int]):
    stack = deque()
    curr = root
    while(len(stack) > 0 or curr!=None):
        while(curr!=None):
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        solution.append(node.val)
        if(node.right):
            curr = node.right    
