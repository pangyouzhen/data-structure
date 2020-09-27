from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left is None and right is None:
            return None
        if left is None:
            return right
        else:
            return left


def createBst(nums: List) -> Optional[TreeNode]:
    # nums.sort()
    if not nums:
        return
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = createBst(nums[:mid])
    root.right = createBst(nums[mid + 1:])
    return root


if __name__ == '__main__':
    a = [i for i in range(1, 10)]
    root = createBst(a)
    left = [i for i in range(1, 3)]
    right = [i for i in range(4, 5)]
    left_node = createBst(left)
    right_node = createBst(right)
    sol = Solution()
    print(sol.lowestCommonAncestor(root, left_node, right_node))
