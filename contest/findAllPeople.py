from typing import List
from collections import defaultdict



class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        a = defaultdict(list)
        for m in meetings:
            a[m[-1]].append(m[0:2])
        init_person = [0, firstPerson]
        k = list(a.keys())
        k.sort()
        for i in k:
            for j in a[i]:
                if set(j) & set(init_person):
                    init_person.extend(j)
        return list(set(init_person))


if __name__ == '__main__':
    func = Solution().findAllPeople
    # n = 6
    # meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    # firstPerson = 1
    n = 5
    meetings = [[3, 4, 2], [1, 2, 1], [2, 3, 1]]
    firstPerson = 1
    print(func(n, meetings, firstPerson))
