# python  *和**
# * 主要解包的是列表
from typing import List

a = [[1, 2, 3, 5]]


def print_a(a: List[int]):
    print(a)


# print_a 输入的是一个List[int], 而a : List[List[int]], 这个时候需要解包
# 就可以写成
print_a(*a)
