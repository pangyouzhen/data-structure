from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def postorder_closure(root):
            if root:
                for i in root.children:
                    postorder_closure(i)
                res.append(root.val)

        postorder_closure(root)
        return res
