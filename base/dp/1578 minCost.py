from typing import List
class Solution:
    #  最直观的解法 -- 超出了时间限制
    def minCost___(self, s: str, cost: List[int]) -> int:
        s = list(s)
        res = 0
        start = 1
        while start < len(s):
            if s[start] == s[start - 1]:
                min_ = min(cost[start], cost[start - 1])
                print(min_)
                if min_ == cost[start - 1]:
                    del s[start - 1]
                    res += cost[start - 1]
                    del cost[start - 1]
                else:
                    del s[start]
                    res += cost[start]
                    del cost[start]
                start -= 1
                print(cost)
            start += 1
        return res

        # 动态规划
    # 1.事件发展的主进程？
    #   前n个字母的最小删除成本
    # 2.定义状态
    #   dp[n]表示前n个字母以第n个字母相同字母结尾的最小删除成本
    # 3.状态转移方程
    #   dp[n] = dp[n-1] + cost[cost_end_index] #剔除当前维护的前n-1个字符中的"末尾字符"
    #   dp[n] = dp[n-1] + cost[n] #剔除第n个字符
    #   dp[n] = dp[n-1] #不是相同字符不做处理
    #   与最后一个字母相同的字母是必要的，那么返回的结果就是dp[-1]
    # l = len(s)
    # process = list(s)
    # dp = [0] * l
    # cost_end_index = 0
    # for n in range(1, l):
    #     # 如果与结尾字母相同
    #     if s[n] == s[n - 1]:
    #         # 从去除上个末尾元素和去除第n个字符中抉择，选取最优删除成本
    #         if cost[cost_end_index] < cost[n]:
    #             dp[n] = dp[n - 1] + cost[cost_end_index]
    #             process[cost_end_index] = -1
    #             cost_end_index = n
    #         else:
    #             dp[n] = dp[n - 1] + cost[n]
    #             process[n] = -1
    #     else:
    #         dp[n] = dp[n - 1]
    #         cost_end_index = n
    # print(process)
    # return dp[-1]


if __name__ == '__main__':
    # s = "abaac"
    # cost = [1, 2, 3, 4, 5]
    # s = "aabaa"
    # cost = [1, 2, 3, 4, 1]
    # s = "aaabbbabbbb"
    # 3+ 5 + 5+ 3+ 5 + 4 +1
    # cost = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
    s = "bbbb"
    # 3+ 5 + 5+ 3+ 5 + 4 +1
    cost = [5, 4, 8, 1]

    sol = Solution()
    print(sol.minCost___(s, cost))
