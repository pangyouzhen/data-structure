# 求解逆序对个数，有1亿个数，每个数的值属于集合{0， 1， 2， 3， 4，5，6，7，8，9}，
# 求只扫描一次的情况下，计算逆序对个数。 说明：[1, 2 ]为顺序对；[4，2]为逆序对
# 例子：输入 - {3，4，3，2，1} ；输出 - 8

a = {0: 0,
     1: 0,
     2: 0,
     3: 0,
     4: 0}

nums = [3, 4, 3, 2, 1]
for i in nums:
    for t in range(i):
        a[t] += 1

print(a)
