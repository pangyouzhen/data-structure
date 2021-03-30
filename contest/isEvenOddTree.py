# Definition for a binary tree node.
from collections import deque

from base.tree.tree_node import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque([root])
        odd = 1
        while q:
            prev = 0 if odd else 10 ** 7
            for _ in range(len(q)):
                root = q.popleft()
                if not root: continue
                #  le, less equivalent <=, ge great equivalent
                comp = int.__le__ if odd else int.__ge__
                if root.val % 2 != odd or comp(root.val, prev): return False
                prev = root.val
                q += (root.left, root.right)
            odd = 1 - odd
        return True


class Solution2:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        vals = {}

        def dfs(root: TreeNode, d: int) -> bool:
            if not root: return True
            if d not in vals: vals[d] = 0 if d % 2 == 0 else 10 ** 7
            comp = int.__ge__ if d % 2 else int.__le__
            if root.val % 2 == d % 2 or comp(root.val, vals[d]): return False
            vals[d] = root.val
            return dfs(root.left, d + 1) and dfs(root.right, d + 1)
        return dfs(root,0)


if __name__ == '__main__':
    tee = TreeNode(1)
    tee.left = TreeNode(10)
    tee.right = TreeNode(4)
    tee.left.left = TreeNode(3)
    tee.right.left = TreeNode(7)
    tee.right.right = TreeNode(9)

    sol = Solution()
    t = sol.isEvenOddTree(tee)
    print(t)
