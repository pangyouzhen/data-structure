"""
# Definition for a Node.
"""
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # bfs
    def connect(self, root: Node) -> Node:
        if root is None:
            return Node()
        result, queue = [], [(root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if node.left:
                queue.append((node.left, depth + 1))
                result.append((node.left.val, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                result.append((node.right.val, depth + 1))
        return result

    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    level.append(cur.left)
                if cur.right:
                    level.append(cur.right)
                if len(q) < 1:
                    cur.next = None
                else:
                    cur.next = q[0]
            q.extend(level)
        return root


if __name__ == '__main__':
    tee = Node(1)
    tee.left = Node(2)
    tee.left.left = Node(4)
    tee.left.right = Node(5)

    tee.right = Node(3)
    tee.right.left = Node(6)
    tee.right.right = Node(7)
    sol = Solution()
    print(sol.connect2(tee))
