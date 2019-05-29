class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_ls = len(matrix[0][0])
        for i in range(len_ls):
            print(matrix[0][i])
            print('_______')


if __name__ == '__main__':
    sol = Solution()
    mat = [
              [1, 2],
              [4, 5],
          ],
    # [
    #     [4,1],
    #     [5,2],
    # ]
    res = sol.rotate(mat)
    print(res)
