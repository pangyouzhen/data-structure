# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            next_level, curr_vals = [], []
            for i in queue:
                if i is not None:
                    curr_vals.append(i.val)
                    for j in i.children:
                        if j:
                            next_level.append(j)
            queue = next_level
            res.append(curr_vals)
        return res
