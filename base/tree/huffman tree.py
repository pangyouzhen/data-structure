# huffman  树是最优二叉树，权重比较高的在前面
from typing import List, Tuple
from heapq import heapify, heappop, heappush
from itertools import count


class Node:
    def __init__(self, x, weight):
        self.x = x
        self.weight = weight
        self.left = None
        self.right = None


# https://www.cnblogs.com/xuchunlin/p/7247346.html
def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(nums)
        heappush(trees, (fa + fb, n, [a, b]))
    return trees[0][-1]


seq = "abcdefghi"
frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
print(huffman(seq, frq))


class Solution:
    def huffman_tree(self, nums: List[Tuple]) -> Node:
        pass

        # 这个肯定不是n次，还有就是每次都进行sorted 是不是有问题了
        #  这边是有问题的，别人的代码使用队列和while，你还在这边算个数 或者别人用heap实现的


if __name__ == '__main__':
    nums = [("a", 1), ("b", 4), ("c", 3), ("d", 2), ("m", 5)]
