class Solution:
    # 暴力解法
    # def buddyStrings(self, s: str, goal: str) -> bool:
    #     _ = list(s)
    #     goal_ls = list(goal)
    #     l = len(s)
    #     for i in range(l):
    #         for j in range(i + 1, l):
    #             _[i], _[j] = _[j], _[i]
    #             if _ == goal_ls:
    #                 return True
    #             _ = list(s)
    #     return False

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


if __name__ == '__main__':
    func = Solution().buddyStrings
    a = "ab"
    goal = "ab"
    print(func(a, goal))
