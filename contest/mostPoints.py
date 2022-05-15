from typing import List



class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            q = questions[i]
            j = i + q[1] + 1
            f[i] = max(f[i+1], q[0]+(f[j] if j < n else 0))
        return f[0]


if __name__ == '__main__':
    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    func = Solution().mostPoints
    print(func(questions))
