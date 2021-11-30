# Definition for a binary tree node.
from typing import List
from collections import Counter

from base.tree.tree_node import TreeNode


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def inorder(root, a):
            if root:
                inorder(root.left, a)
                a.append(root.val)
                inorder(root.right, a)

        a = []
        inorder(root, a)
        temp = Counter(a).most_common()
        freq = temp[0][1]
        result = [i[0] for i in temp if i[1] == freq]
        return result


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(2)
    sol = Solution()
    print(sol.findMode(tree))
