from typing import List
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        N = len(envelopes)
        envelopes.sort()
        res = 0
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def maxEnvelopes_2(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num

        return len(f)


if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    sol = Solution()
    print(sol.maxEnvelopes(envelopes))
