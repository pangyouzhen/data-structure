from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        a = 0
        while a < len(arr):
            if arr[a] > arr[a + 1]:
                return a
            a += 1


if __name__ == '__main__':
    arr = [0, 1, 0]
    func = Solution().peakIndexInMountainArray
    print(func(arr))
