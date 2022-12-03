from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count_ = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count_ += 1
        return count_


if __name__ == '__main__':
    sol = Solution()
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    print(sol.busyStudent(startTime, endTime, queryTime))
