# 2) dict

# 3)  lru_cache
from functools import lru_cache


@lru_cache()
def f():
    pass


# 4）list
# 注意使用zip和enumetre 方法

# 5）tree
# python 没有内置的树方法，需要自己定义


#  python 求交并差集 使用集合进行判断

a = {"a1", "a2", "b1"}
b = {"b1", "b2", "a1"}

# 交集
print(a & b)
print(a - b)
print(b - a)
print(a | b)
