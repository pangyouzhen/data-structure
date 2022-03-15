from typing import List
from pysnooper import snoop

class Solution:
    # @snoop()
    # def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
    #     self.breaks = []
    #
    # @lru_cache()
    # def dfs(self, goal: int, i: int):
    #     # 深度优先的情况: start 在里面，有终止条件，如果结果是-1，没终止条件
    #     if start:
    #         pass
    #     for i in nums:
    #         for j in [goal - i, goal + i, goal ^ i]:
    pass

    # @snoop()
    # TODO 广度优先算法，没写出来
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        goals = {goal}
        goals_break = set()
        times = 0
        while goals:
            times += 1
            for goal in goals:
                # 每一层的goals
                if goal not in goals_break:
                    goals_break.add(goal)
                for i in nums:
                    goals = set(j for j in [goal - i, goal + i, goal ^ i])
                    if start in goals:
                        return times
            print(goals)
            t = []
            for g in goals:
                if g < 0 or g > 1000:
                    t.append(g)
            goals = goals - set(t)
        return -1


if __name__ == '__main__':
    # nums = [1, 3]
    # start = 6
    # goal = 4
    # nums = [2, 8, 16]
    # start = 0
    # goal = 1
    nums = [1]
    start = 0
    goal = 3
    func = Solution().minimumOperations
    print(func(nums, start, goal))
