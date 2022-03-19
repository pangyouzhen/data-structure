from typing import Optional

from base.tree.tree import TreeNode

# TODO
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"


if __name__ == "__main__":
    func = Solution().tree2str
    tree = TreeNode.from_strs("[1,2,3,4]")
    print(tree)
    print(func(tree))
