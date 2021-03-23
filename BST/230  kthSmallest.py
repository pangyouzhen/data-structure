from base.tree.tree_node import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = []

        def inorder(root, a):
            if len(a) == k:
                return
            if root:
                inorder(root.left, a)
                a.append(root.val)
                inorder(root.right, a)

        inorder(root, a)
        return a[k-1]


if __name__ == '__main__':
    treeNode = TreeNode(3)
    treeNode.left = TreeNode(1)
    treeNode.right = TreeNode(4)
    treeNode.left.right = TreeNode(2)
    sol = Solution()
    print(sol.kthSmallest(treeNode, 1))
