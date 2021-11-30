from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        pass


if __name__ == '__main__':
    sol = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    new_color = 2
    print(sol.floodFill(image, sr, sc, new_color))
