class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        # 代码1
        # if not root:
        #     return 0
        # res = []
        # if root.children:
        #     for i in root.children:
        #         res.append(self.maxDepth(i) + 1)
        # return max(res)

        # 代码2 代码1和代码2的根本区别是？
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1


if __name__ == '__main__':
    node_left_left = Node(5, children=[])
    node_left_right = Node(6, children=[])
    node_left = Node(3, children=[node_left_left, node_left_right])
    node_center = Node(2, children=[])
    node_right = Node(4, children=[])
    node = Node(1, children=[node_left, node_center, node_right])
    sol = Solution()
    print(sol.maxDepth(node))
