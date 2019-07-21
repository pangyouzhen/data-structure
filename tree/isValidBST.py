# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode):
        if root is None:
            return True
        return self.isValidBSTRec(root)

    def isValidBSTRec(self, root: TreeNode):
        # 3 step:
        #  Tree problem -> travserd -> two parts -> the second part need some element
        # 1. None ->  True
        # 2. False
        # 3. travserd the  until True or Flase
        # ptr is ALL
        if root is None:
            return True
        if root.left is not None and root.val <= root.left.val:
            return False
        if root.right is not None and root.val >= root.right.val:
            return False
        return self.isValidBSTRec(root.left) and self.isValidBSTRec(root.right)


if __name__ == '__main__':
    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3)
    sol = Solution()
    assert sol.isValidBSTRec(tree1) == True

    tree2 = TreeNode(5)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(4)
    tree2.right.left = TreeNode(3)
    tree2.right.right = TreeNode(6)
    assert sol.isValidBSTRec(tree2) == False

    tree3 = TreeNode(1)
    tree3.left = TreeNode(1)
    assert sol.isValidBSTRec(tree3) == False
