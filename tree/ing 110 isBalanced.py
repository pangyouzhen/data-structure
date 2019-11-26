class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode):
        if root is None:
            return True

        def get_height(root):
            if root is None:
                return 0
            left_height, right_height = get_height(root.left), get_height(root.right)
            return max(left_height, right_height) + 1
        left = root.left
        right = root.right
        if abs(get_height(left) - get_height(right)) > 1:
            return False
        return True


if __name__ == '__main__':
    p1 = TreeNode(3)
    p1.left = TreeNode(9)
    p1.right = TreeNode(20)
    p1.right.left = TreeNode(15)
    p1.right.right = TreeNode(7)

    sol = Solution()
    assert sol.isBalanced(p1) == True

    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    p2.right = TreeNode(2)
    p2.left.left = TreeNode(3)
    p2.left.right = TreeNode(3)
    p2.left.left.left = TreeNode(4)
    p2.left.left.right = TreeNode(4)

    assert sol.isBalanced(p2) == False

    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(2)
    p3.left.left = TreeNode(3)
    p3.right.right = TreeNode(3)
    p3.left.left.left = TreeNode(4)
    p3.left.right.right = TreeNode(4)

    assert sol.isBalanced(p3) == False
