from typing import List
from string import ascii_uppercase


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        case_start, case_end = s[0], s[3]
        num_start, num_end = int(s[1]), int(s[4])

        res = []
        if case_start == case_end:
            for j in range(num_start, num_end + 1):
                res.append(case_start + str(j))
            return res
        start = False
        for i in ascii_uppercase:
            if i == case_start:
                for j in range(num_start, num_end + 1):
                    res.append(i + str(j))
                start = True
            elif i == case_end:
                for j in range(num_start, num_end + 1):
                    res.append(i + str(j))
                return res
            if start is True and i != case_start:
                for j in range(num_start, num_end + 1):
                    res.append(i+str(j))

if __name__ == '__main__':
    s = "K1:L2"
    s1 ="A1:F1"
    s2 = "W5:W8"
    func = Solution().cellsInRange
    print(func(s))
    print(func(s1))
    print(func(s2))