from typing import List

class Solution():
    def generateMatrix(self, n: int) -> List[List[int]]:
        diretion = [[0,1],[0,-1],[1,0],[-1,0]]
        nums = [[i,j] for i in range(n) for j in range(n)]
        pass
            

if __name__ =="__main__":
    func = Solution().generateMatrix
    n = 3
    print(func(n))