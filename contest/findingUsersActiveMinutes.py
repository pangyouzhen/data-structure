from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        a = {}
        for i in logs:
            if i[0] not in a:
                a[i[0]] = [i[1]]
            else:
                a[i[0]].append(i[1])

        for k, v in a.items():
            t = len(set(v))
            res[t - 1] += 1
        return res


if __name__ == '__main__':
    logs = [[1, 1], [2, 2], [2, 3]]
    k = 4
    sol = Solution()
    print(sol.findingUsersActiveMinutes(logs, k))
