# Definition for a binary tree node
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeInOrder:

    def PreOrder(self, root):
        if root is None:
            return

        print(root.val)
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self, root):
        if root is None:
            return

        self.InOrder(root.left)
        print(root.val)
        self.InOrder(root.right)

    def PostOrder(self, root):
        if root is None:
            return

        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val)


if __name__ == '__main__':
    treeNode = TreeNode(25)
    treeNode.left = TreeNode(3)
    treeNode.right = TreeNode(4)
    treeNode.left.left = TreeNode(5)
    treeNode.left.right = TreeNode(6)

    treeInOrder = TreeInOrder()
    treeInOrder.PreOrder(treeNode)
    print("--------")
    treeInOrder.InOrder(treeNode)
    print("*****")
    treeInOrder.PostOrder(treeNode)
