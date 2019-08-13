# class TreeNode:
#     def __int__(self, val):
#         self.val = val
#         self.left = None
#         self.right= None

# TODO why above def not work
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    treeNode = TreeNode(1)
    treeNode.left = TreeNode(5)
    treeNode.right = TreeNode(7)
    treeNode.left.left = TreeNode(3)
    treeNode.left.right = TreeNode(6)

    sol = Solution()
    result = sol.preorderNonRecursive(treeNode)
    print(result)