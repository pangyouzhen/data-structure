from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        keyvalues = sorted(nums_counter.items(), key=lambda x: (x[0], x[1]))
        start = 0
        var = 0
        while start < len(keyvalues) - 1:
            if keyvalues[start + 1][0] - keyvalues[start][0] != 1:
                pass
            else:
                temp = keyvalues[start + 1][1] + keyvalues[start][1]
                if temp > var:
                    var = temp
            start += 1
        return var


if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    sol = Solution()
    print(sol.findLHS(nums))
