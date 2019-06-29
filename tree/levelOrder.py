class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        memo = []
        memo.append([root.val])
        return self.levelOrderRec(root.left, root.right, memo)

    def levelOrderRec(self, left, right, memo):
        level = []
        if left is None and right is None:
            return memo
        if left:
            level.append(left.val)
        if right:
            level.append(right.val)
        memo.append(level)
        left_value = self.levelOrderRec(left.left, left.right, memo)
        right_value = self.levelOrderRec(right.left, right.right, memo)
        return


if __name__ == '__main__':
    tee = TreeNode(3)
    tee.left = TreeNode(9)
    tee.right = TreeNode(20)
    tee.right.left = TreeNode(15)
    tee.right.right = TreeNode(7)

    sol = Solution()
    # assert sol.levelOrder(tee) == [[3], [9, 20], [15, 7]]
    print(sol.levelOrder(tee))
