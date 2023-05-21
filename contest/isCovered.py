from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for i in range(left, right + 1):
            flag = []
            for start, end in ranges:
                if end >= i >= start:
                    flag.append(True)
                else:
                    flag.append(False)
            if len(flag) == len(ranges):
                if not any(flag):
                    return False
        return True


if __name__ == '__main__':
    func = Solution().isCovered
    ranges = [[1, 2], [3, 4], [5, 6]]
    left = 2
    right = 5
    print(func(ranges, left, right))
