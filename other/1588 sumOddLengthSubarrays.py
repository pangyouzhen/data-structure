from builtins import int
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum1 = 0
        for i in range(1, len(arr) + 2, 2):
            # 5 - 3 +1 = 3
            for j in range(len(arr) - i + 1):
                # print(f"{i = }-----{arr[j:j + i] = }")
                sum1 += sum(arr[j:j + i])
        return sum1


#  1 <= arr.length <= 100
#  1 <= arr[i] <= 1000

if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    # 所以时间复杂度 可以为 O(n^2)
    sol = Solution()
    temp = sol.sumOddLengthSubarrays(arr)
    print(temp)
