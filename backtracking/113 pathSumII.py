# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#  错误的，想仿照排列数和组合数进行回溯，因为是树型结构，但是没成功
class Solution:
    class Solution:
        def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
            ret = list()
            path = list()

            def dfs(root: TreeNode, total: int):
                if not root:
                    return
                path.append(root.val)
                total -= root.val
                if not root.left and not root.right and total == 0:
                    ret.append(path[:])
                dfs(root.left, total)
                dfs(root.right, total)
                path.pop()

            dfs(root, total)
            return ret



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
