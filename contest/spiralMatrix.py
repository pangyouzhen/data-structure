from typing import List, Optional, Tuple


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        a = [[-1] * n for i in range(m)]
        k = 0
        order = self.spiralOrder(a)
        while head:
            val = head.val
            i,j = order[k]
            a[i][j] = val
            head = head.next
            k += 1
        return a
    


    def spiralOrder(self, matrix: List[List[int]]) -> List[Tuple[int,int]]:
        if not matrix or not matrix[0]:
            return list()
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        res = [(0,0)]
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
            res.append((row,column))
        return res

if __name__ == "__main__":
    func = Solution().spiralOrder
    a = [[-1] * 5 for i in range(3)]
    print(func(a))