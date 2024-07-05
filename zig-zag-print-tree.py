# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We will do the Standard BFS Solution with None as our Delimiter for ending
        # a level ...
        if root == None:
            return []
        queue = deque([root, None])
        is_order_left = True
        results = []
        level_queue = deque()
        while(len(queue) != 0):
            node = queue.popleft()
            if node:
                if is_order_left:
                    level_queue.append(node.val)
                else:
                    level_queue.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                # print(level_queue)
                results.append(level_queue)
                level_queue = deque()
                is_order_left = not is_order_left
                if len(queue) > 0:
                    queue.append(None)
        return results
