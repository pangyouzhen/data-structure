from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        # not used rec
        if root is None:
            return []
        result, queue = [], [root]
        while queue:
            next_level, vals = [], []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            result.append(vals)
        return result


if __name__ == '__main__':
    tee = TreeNode(3)
    tee.left = TreeNode(9)
    tee.right = TreeNode(20)
    tee.right.left = TreeNode(15)
    tee.right.right = TreeNode(7)

    sol = Solution()
    t = sol.levelOrder(tee)
    print(t)
    # assert sol.levelOrder(tee) == [[3], [9, 20], [15, 7]]
    # print(sol.levelOrder(teeleft))