from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序，后续，中序 的不同指出和名称的意思 在于打印root value的位置不同

class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    #  root 1 left-mid 3 left-left 4 left right 5 / right 2
    #  stack -> [1,3,2,4,5] + [3,4,5] + [4]
    #  res +[4] + [3] + [5]

    def inorder(self, root: TreeNode):
        self.inorderRecNew(root)
        return self.result

    def inorderRecNew(self, root):
        if root:
            self.inorderRecNew(root.left)
            self.result.append(root.val)
            self.inorderRecNew(root.right)


if __name__ == '__main__':
    sol = Solution()
    treenode = TreeNode(10)
    treenode.right = TreeNode(5)
    treenode.left = TreeNode(11)
    treenode.right.left = TreeNode(6)
    treenode.right.right = TreeNode(3)
    # treenode.right.left = TreeNode(3)
    # print(sol.simpleInorder(treenode))
    # print(sol.inorderRecursive(treenode))
    print(sol.inorderTraversal(treenode))
    # print(sol.inorderRec(treenode))
    print(sol.inorder(treenode))
