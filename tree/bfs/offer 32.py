# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        queue_val = [0]
        while queue:
            head = queue.pop(0)
            head_val = queue.pop(0)
            if head.right:
                queue.append(head.right)
                queue_val.append(head_val + 1)
            if head.left:
                queue.append(head.left)
                queue_val.append(head_val + 1)
