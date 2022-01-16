from typing import List
from collections import defaultdict


class Solution:
    # todo
    def mostPoints(self, questions: List[List[int]]) -> int:
        a = defaultdict(int)
        l = len(questions)
        dp = [0] * l
        dp[0] = questions[0][0]
        for i, v in enumerate(questions):
            a[i] = i + questions[i][1]
            reverse_dic = {val: key for key, val in a.items()}
            if i == 0:
                dp[i] = max(dp[i - 1],questions[i][0])
            else:
                dp[i] = dp[reverse_dic[i]] + questions[i][0]
        return dp[-1]


if __name__ == '__main__':
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    func = Solution().mostPoints
    print(func(questions))
