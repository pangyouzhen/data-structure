from copy import deepcopy


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        scores = 0

        def dfs(points, k, l, r, scores):
            if k == 1:
                return max(points[l], points[r])
            l_max = dfs(points, k-1, l+1, r, scores) + scores[l]
            r_max = dfs(points, k-1, l, r-1, scores) + points[r]

            return max(l_max, r_max)

        return dfs(cardPoints, k, 0, len(cardPoints)-1, scores)
