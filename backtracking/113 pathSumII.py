# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        # def dfs(graph, start, visited=None):
        #     if visited is None:
        #         visited = set()
        #     visited.add(start)
        #     for next_ in graph[start] - visited:
        #         dfs(graph, next_, visited)
        #     return visited
        if not root:
            return []

        res = []

        def helper(root, ans, tmp):
            if ans == 0 and not root.left and not root.right:
                res.append(tmp)
            if root.left:
                helper(root.left, ans - root.left.val, tmp + [root.left.val])
            if root.right:
                helper(root.right, ans - root.right.val, tmp + [root.right.val])

        helper(root, sum - root.val, [root.val])
        return res


if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)
    sol = Solution()
    print(sol.pathSum(tree, 22))
