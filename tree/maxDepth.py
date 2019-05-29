# Definition for a binary tree node.
# 插入，删除，查找
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        pass


if __name__ == '__main__':
    sol = Solution()
    res = sol.maxDepth([3, 9, 20, 'null', 'null', 15, 7])
    # [3, [9, ['null', 'null']], 20, [15, 7]]
    print(res)
