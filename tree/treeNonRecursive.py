# class TreeNode:
#     def __int__(self, val):
#         self.val = val
#         self.left = None
#         self.right= None

# TODO why above def not work
from base.tree.tree_node import TreeNode


class Solution:
    def preorderNonRecursive(self, root):
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res


if __name__ == '__main__':
    nums = [1, 5, 7, 3, 6]
    tree = TreeNode.from_list(nums)
    print(tree)
    sol = Solution()
    result = sol.preorderNonRecursive(tree)
    print(result)
