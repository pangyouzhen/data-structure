from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# todo
class Solution:

    def __init__(self) -> None:
        self.res = []

    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res

    #         bfs + heap_queue
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        self.binaryTreePaths_(self, root)
        return self.res

    def binaryTreePaths_(self, root: TreeNode):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.res.append()


if __name__ == '__main__':
    treeNode = TreeNode(1)
    treeNode.left = TreeNode(2)
    treeNode.left.right = TreeNode(5)
    treeNode.right = TreeNode(3)
    sol = Solution()
    print(sol.binaryTreePaths(treeNode))
