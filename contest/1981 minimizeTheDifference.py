from typing import List

# TODO
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        pass
if __name__ == '__main__':
    # mat = [[1], [2], [3]]
    # target = 100
    mat = [[1, 2, 9, 8, 7]]
    target = 6
    func = Solution().minimizeTheDifference
    print(func(mat, target))
