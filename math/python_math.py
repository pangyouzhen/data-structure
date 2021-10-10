# 用python基础类实现一些常见的操作
# 计算列表中的众数
from collections import Counter
from typing import Tuple, List
import numpy as np

a = [1, 2, 3, 4, 5, 6, 6]
c = Counter(a)
t: List[Tuple] = c.most_common(3)
print(t)


# 计算列表中的中位数
# 中位数常见解决绝对值求和的极值最值问题
def median(data):
    data.sort()
    length = len(data)
    if (length % 2) == 1:
        z = length // 2
        y = data[z]
    else:
        y = (data[length // 2] + data[length // 2 - 1]) / 2
    return y


b = [1, 2, 3, 5, 6, 6]
assert median(b) == np.median(b)
print(median(b))
assert median(a) == np.median(a)
print(median(a))

# 矩阵的转置
m: List[List[int]] = [[1, 2, 3], [4, 5, 6]]
print(np.transpose(m).tolist())
m_len = len(m)
element_len = len(m[0])
reversed_matrix = [[None] * m_len for i in range(element_len)]
for i in range(m_len):
    for j in range(element_len):
        reversed_matrix[j][i] = m[i][j]
print(reversed_matrix)
#
