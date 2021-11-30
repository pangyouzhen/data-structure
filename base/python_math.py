# 用python基础类实现一些常见的操作
# 计算列表中的众数
from collections import Counter
from typing import Tuple, List
import numpy as np

a = [1, 2, 3, 4, 5, 6, 6]
c = Counter(a)
t: List[Tuple] = c.most_common(3)


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
assert median(a) == np.median(a)

# 矩阵的转置
m: List[List[int]] = [[1, 2, 3], [4, 5, 6]]
m_len = len(m)
element_len = len(m[0])
reversed_matrix = [[None] * m_len for i in range(element_len)]
for i in range(m_len):
    for j in range(element_len):
        reversed_matrix[j][i] = m[i][j]
print(f"{reversed_matrix = }")
#

# 打印矩阵，理解两层循环
r = 3
c = 3
# 这种和设想的不一样在于矩阵的每一个元素用[]表示
matrix = [[i, j] for i in range(r) for j in range(c)]
# 这个得到的是9 * 2 的，可以用来枚举 字符串start end
matrix_temp = [[i for i in range(r)] for j in range(c)]
# 这个得到的才是3 * 3的方阵
print(f"{matrix = }")
print(f"{matrix_temp = }")

# 打印矩阵的上三角，可以用来构建索引，理解for循环等操作，带对角线
matrix2 = [[i, j] for i in range(r) for j in range(i, c)]
print(f"{matrix2 = }")
# 上三角，不带对角线
matrix2 = [[i, j] for i in range(r) for j in range(i + 1, c)]
print(f"{matrix2 = }")
# 打印矩阵的下三角，不带对角线
matrix3 = [[i, j] for i in range(r) for j in range(i)]
print(f"{matrix3 = }")
# 打印矩阵的下三角，带对角线
matrix3 = [[i, j] for i in range(r) for j in range(i + 1)]
print(f"{matrix3 = }")
s = "abcde"
# 枚举所有子串
for i in range(len(s)):
    # [0, l) 数学表示
    # 这里起始值设置为i+1,避免空串，末尾设置为len(s)+1的主要原因是s[i:j]，切片时是不包含末尾的
    for j in range(i + 1, len(s) + 1):
        # [j,l) 数学表示
        print(s[i:j])


# 固定长度的滑动窗口,以2为例
_ = "abcde"
# 只有最后k-1个元素没法进行滑动，所以长度应该len -k +1
for i in range(len(_) - 2 + 1):
    print(_[i:i + 2])

# 矩阵转置,以不规则matrix为例,原始是9*2,所以reverse得到的是2 * 9的
r = len(matrix)
# 9
c = len(matrix[0])
# 2
reverse_ = [[None] * r for i in range(c)]
# print(reverse_)
for i in range(r):
    for j in range(c):
        reverse_[j][i] = matrix[i][j]
print(reverse_)


# 分组
# 均等分组 将0->(num-1)的组分为group组, 假设可以均分
def equal_group(num: int, group_num: int) -> List[List[int]]:
    nums = [i for i in range(num)]
    res = []
    k = group_num
    element_num = int(num / group_num)
    for i in range(k):
        res.append(nums[i * element_num:(i + 1) * element_num])
    return res


print(equal_group(100, 25))


# 递增分组 第一组1个，第二组2个，第三组3个，第四组4个.....
def increase_group(num: int) -> List[List[int]]:
    i = 0
    res = []
    tmp = []
    group = 1
    while i < num:
        tmp.append(i)
        #  这里改一下就是递乘分组了 group * n
        if len(tmp) == group:
            res.append(tmp)
            tmp = []
            group += 1
        i += 1
    return res
