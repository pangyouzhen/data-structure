# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode):
        return self.isValidBSTRec(root, lessThan=float('inf'), largerThan=float('-inf'))

    def isValidBSTRec(self, root: TreeNode, lessThan, largerThan):
        # 3 step:
        #  Tree problem -> travserd -> two parts -> the second part need some element
        # 1. None ->  True
        # 2. False
        # 3. travserd the  until True or Flase
        # ptr is ALL
        if root is None:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBSTRec(root.left, min(lessThan, root.val), largerThan) and self.isValidBSTRec(root.right,
                                                                                                         lessThan,
                                                                                                         max(root.val,
                                                                                                             largerThan))


if __name__ == '__main__':
    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3)
    sol = Solution()
    assert sol.isValidBST(tree1) == True

    tree2 = TreeNode(5)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(4)
    tree2.right.left = TreeNode(3)
    tree2.right.right = TreeNode(6)
    assert sol.isValidBST(tree2) == False

    tree3 = TreeNode(1)
    tree3.left = TreeNode(1)
    assert sol.isValidBST(tree3) == False
