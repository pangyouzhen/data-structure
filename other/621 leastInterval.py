from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        counter = Counter(tasks)
        k = max(counter.values())
        #  一共有k-1组，每组 n + 1个元素，最后一组没有idle
        #  最后一个个数怎么确定？
        #  A A A B B B    n=2
        maxCount = sum(1 for v in counter.values() if v == k)
        v = (k - 1) * (n + 1) + maxCount
        return max(v, l)
