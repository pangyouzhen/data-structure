# python 中的数据结构
# 1. 队列
# 1) Queue模块：
import queue

# 优先级队列
queue.PriorityQueue()
# 后入先出队列 -> 栈
queue.LifoQueue()
# python  使用list就可以定义
# 先入先出队列
queue.Queue(maxsize=4)

# 2) Collections
from collections import deque

# deque 双向队列
deque(maxlen=4)

# 2) dict
# python 3.6 后默认 dict 是有序的了

# 3)  lru_cache
from functools import lru_cache


@lru_cache()
def f():
    pass

# 4）list
# 注意使用zip和enumetre 方法

# 5）tree
# python 没有内置的树方法，需要自己定义
