from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in trust:
            d[i[0]].append(i[1])
        all_persons = set(range(1, n + 1))
        judge_person = all_persons - set(d.keys())
        if len(judge_person) != 1:
            return -1
        else:
            judge_person = list(judge_person)[0]
            for j in d.values():
                if judge_person not in j:
                    return -1
            return judge_person


if __name__ == '__main__':
    func = Solution().findJudge
    n = 2
    trust = [[1, 2]]
    print(func(n, trust))
