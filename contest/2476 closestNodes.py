# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
import bisect

from base.tree.tree import TreeNode


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a = []

        def dfs(roots: TreeNode):
            if roots:
                dfs(roots.left)
                a.append(roots.val)
                dfs(roots.right)
        
        dfs(root)
        res = []
        s = set(a)
        for q in queries:
            if q in s:
                res.append([q, q])
                continue
            ind = bisect.bisect(a, q)
            # left 
            rl = -1 if ind == 0 else a[ind - 1]
            # right
            rr = -1 if ind == len(a) else a[ind]
            res.append([rl, rr])
        return res


if __name__ == "__main__":
    func = Solution().closestNodes
    root = "[6,2,13,1,4,9,15,null,null,null,null,null,null,14]"
    queries = [2, 5, 16]
    tree = TreeNode.from_strs(root)
    print(func(tree, queries))
