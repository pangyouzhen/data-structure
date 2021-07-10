from collections import defaultdict
from bisect import bisect
import pysnooper

# todo
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    @pysnooper.snoop()
    def get(self, key: str, timestamp: int) -> str:
        val = self.d.get(key)
        val_dict = dict(val)
        a = list(val_dict.keys())
        a.sort()
        if timestamp in a:
            return val_dict[timestamp]
        else:
            ind = bisect(a, timestamp)
            return val_dict[a[ind - 1]]


if __name__ == '__main__':
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    param_2 = obj.get("foo", 1)
    print(obj.get("foo", 3))  # 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"）
    obj.set("foo", "bar2", 4)
    print(obj.get("foo", 4))  # 输出 "bar2"
    print(obj.get("foo", 5))  # 输出 "bar2"
