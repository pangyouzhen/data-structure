from typing import List
from string import ascii_lowercase


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i, v in zip(ascii_lowercase, distance):
            if i in s:
                start_index = s.index(i)
                new_index = start_index + v + 1
                if new_index >= len(s):
                    return False
                if s[new_index] != i:
                    return False
        return True


if __name__ == '__main__':
    func = Solution().checkDistances
    s = "abaccb"
    d = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s2 = "aa"
    d2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(func(s, d))
    print(func(s2, d2))
