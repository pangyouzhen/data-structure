from typing import Optional, List

from base.tree.tree_node import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: TreeNode) -> str:
            if not node:
                return ''
            serial = ''.join([str(node.val), '(', dfs(node.left), ')(', dfs(node.right), ')'])
            print(serial)
            tree = seen.get(serial, None)
            if tree:
                repeat.add(tree)
            else:
                seen[serial] = node
            return serial

        seen = dict()
        repeat = set()
        dfs(root)
        return list(repeat)


if __name__ == '__main__':
    root = TreeNode.from_strs("[2,1,1]")
    root2 = TreeNode.from_strs("[1,2,3,4,null,2,4,null,null,4]")
    print(root2)
    func = Solution().findDuplicateSubtrees
    print(func(root2))
    # print(func(root2))
