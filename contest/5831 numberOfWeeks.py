from typing import List
from bisect import insort
import pysnooper


class Solution:
    @pysnooper.snoop()
    def numberOfWeeks(self, milestones: List[int]) -> int:
        queue = sorted(milestones, reverse=True)
        result = 0
        # 动态更新的栈
        while len(queue) > 1:
            init = queue[0] - queue[1] - 1
            queue.pop(0)
            queue.pop(0)
            if init <= 0:
                result += queue[1] * 2 + 1
            else:
                insort(queue, init)
        return result


if __name__ == '__main__':
    sol = Solution().numberOfWeeks
    milestones = [5, 2, 1]
    print(sol(milestones))
