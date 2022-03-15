from typing import List
from collections import defaultdict
from bisect import bisect


class Solution:
    # TODO
    def getOrder(self, task: List[List[int]]):
        task_dict = defaultdict(list)
        for ind, (start_time, last_time) in task:
            # 增加索引, 放入的时候就排好序，
            task_dict[start_time].append([last_time, ind])
        # 第一个开始执行的时间
        start_ = min(task_dict.keys())
        fst_list = sorted(task_dict[start_], key=lambda x: x[0])
        # 从开始到结束时间
        fst_last = start_ + fst_list[0][0]
        inds = [fst_list[0][1]]
        task.pop(fst_list[0][1])
        while task:
            # 找到从开始到结束时间内的所有可执行任务
            for k, v in task_dict.items():
                pass


if __name__ == '__main__':
    tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    sol = Solution()
    print(sol.getOrder(tasks))
