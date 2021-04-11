from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def preorder_closure(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    preorder_closure(i)

        preorder_closure(root)
        return res


if __name__ == '__main__':
    sol = Solution()
