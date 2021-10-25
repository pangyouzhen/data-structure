from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 时间复杂度 O(m * n)
        for row in matrix:
            for val in row:
                if val == target:
                    return True
                elif val > target:
                    break
        return False
