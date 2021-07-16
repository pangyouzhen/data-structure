from collections import defaultdict
from bisect import bisect_right
import pysnooper
import importlib
import inspect


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append([timestamp, value])

    @pysnooper.snoop()
    def get(self, key: str, timestamp: int) -> str:
        # return "" if (a := bisect_right(self.dct[key], [timestamp, "z" * 101])) == 0 else self.dct[key][a - 1][1]
        a = bisect_right(self.dct[key], [timestamp, "z" * 101])
        if a == 0:
            return ""
        else:
            return self.dct[key][a - 1][1]


def import_main_class(module_path=None):
    """Import a module at module_path and return its main class:
    - a DatasetBuilder if dataset is True
    - a Metric if dataset is False
    """
    from pathlib import Path
    if module_path is None:
        module_path = Path(__file__).stem
    module = importlib.import_module(module_path)
    main_cls_type = type

    # Find the main class in our imported module
    module_main_cls = None
    for name, obj in module.__dict__.items():
        if isinstance(obj, type):
            if inspect.isabstract(obj):
                continue
            module_main_cls = obj
            break

    return module_main_cls


# if __name__ == '__main__':
    # obj = TimeMap()
    # obj.set("foo", "bar", 1)
    # param_2 = obj.get("foo", 1)
    # print(obj.get("foo", 3))  # 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"）
    # obj.set("foo", "bar2", 4)
    # print(obj.get("foo", 4))  # 输出 "bar2"
    # print(obj.get("foo", 5))  # 输出 "bar2"
