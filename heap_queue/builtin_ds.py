# python 中的数据结构
# 1. 队列
# 1) Queue模块：
import queue

# 优先级队列
customers: queue.PriorityQueue = queue.PriorityQueue()
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((1, "Harry"))
customers.put((4, "Stacy"))
while not customers.empty():
    print(customers.get())
# 后入先出队列 -> 栈
queue.LifoQueue()
# python  使用list就可以定义
# 先入先出队列
queue.Queue(maxsize=4)

# 2) Collections
from collections import deque

# deque 双向队列
deque(maxlen=4)