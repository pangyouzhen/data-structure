# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return []
        result, current = [], [root]
        level = -1
        result_bool = False
        while current:
            level += 1
            if level == 0:
                if root.val % 2 == 0:
                    return False
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            if level % 2 == 0:
                result_bool = self.is_increse(vals)
            else:
                result_bool = self.is_decrease(vals)
            if result_bool:
                continue
            else:
                return result_bool
        return result_bool

    def is_increse(self, vals):
        a = vals[0]
        for i in vals[1:]:
            if i % 2 != 0:
                if i > a:
                    a = i
                    continue
                else:
                    return False
            else:
                return False
        return True

    def is_decrease(self, vals):
        a = vals[0]
        for i in vals[1:]:
            if i % 2 == 0:
                if i < a:
                    a = i
                    continue
                else:
                    return False
            else:
                return False
        return True


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
