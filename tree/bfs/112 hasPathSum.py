class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        # 题目中说的是叶子节点
        if root.left is None and root.right is None:
            return root.val == sum
        if self.hasPathSum(root.left, sum - root.val):
            return True
        if self.hasPathSum(root.right, sum - root.val):
            return True
        return False

    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [root]
        que_val = [root.val]
        while queue:
            head = queue.pop(0)
            head_val = que_val.pop(0)
            if not head.left and not head.right:
                if head_val == sum:
                    return True
                continue
            if head.right:
                queue.append(head.right)
                que_val.append(head_val + head.right.val)
            if head.left:
                queue.append(head.left)
                que_val.append(head_val + head.left.val)
        return False


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
    print(sol.hasPathSum2(tree, 22))
