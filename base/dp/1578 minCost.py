from typing import List
from copy import deepcopy


#  最小删除成本 -> 首先考虑动态规划


#  这个使用的是DP
#  如果新增数字和前面的不一样，则总cost不变
#  dp[i+1] = dp[i] + 0 if s[i] != s[i+1]
#  动态规划的两种思想
#  1. 记忆化搜索，可以想象成一棵树，这棵树进行 递归，-> 状态转移方程，存在许多的重复值，需要进行剪枝，
#  剪枝就把原先计算好的保留, 根节点是 目标值，比如总共花费27
#  2. 按顺序推导（数学归纳），假设原先的已经成立，增加一个元素怎么处理
#  这个题目的问题是 "bbbb" 和 cost = [5, 4, 8, 1]， 当
#  a = [b]  min = 0 不用管
#  a = [b,b] min = (5,4) 比较，所以应该删除 4 的那个，保留大的元素
#  a = [b,b,b] min = (5,8) 所以应该删除5的元素那个，写代码时，
#  这个容易写成和前一个元素比较，而不是和删除了最小值的前一个元素比较, 所以需要维护一个索引值
class Solution:
    # def minCost(self, s: str, cost: List[int]) -> int:
    #     res = 0
    #     for i, v in enumerate(s[1:]):
    #         if s[i + 1] == s[i]:
    #             t = min(cost[i + 1], cost[i])
    #             res += t
    #             print(t)
    #     return res
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

# 动态规划，什么情况下用 动态规划
# 1. 计数
# 2. 最值，最长递升子序列
# 3. 是否
