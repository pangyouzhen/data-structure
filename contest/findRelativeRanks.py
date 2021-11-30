from typing import List
import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        negativate_score = [-i for i in score]
        # heapq.heapify(negativate_score)
        negativate_score.sort()
        k = 1
        for i in negativate_score:
            ind: int = score.index(-i)
            if k == 1:
                score[ind] = "Gold Medal"
            elif k == 2:
                score[ind] = "Silver Medal"
            elif k == 3:
                score[ind] = "Bronze Medal"
            else:
                score[ind] = str(k)
            k += 1
        return score


if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    func = Solution().findRelativeRanks
    print(func(nums))
