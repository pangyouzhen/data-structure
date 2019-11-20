class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def traverse(self, root: Node):
        res = []
        thislevel = [root]
        while thislevel:
            nextlevel = list()
            for i in thislevel:
                res.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            thislevel = nextlevel
        return res


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.right = Node(6)
    sol = Solution()
    print(sol.traverse(tree))
