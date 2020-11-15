from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = []
        for i, v in enumerate(arr[:-1]):
            a.append(arr[i + 1:])
        a.append(-1)
        return a


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    sol = Solution()
    print(sol.replaceElements(arr))
