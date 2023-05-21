from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1 = self.score(player1)
        s2 = self.score(player2)
        if s1 == s2:
            return 0
        elif s1 > s2:
            return 1
        else:
            return 2

    def score(self, player: List[int]) -> int:
        s = 0
        last2 = False
        t = 0
        for i, v in enumerate(player):
            if t >= 2:
                last2 =False
            if last2:
                s = s + 2*v
            else:
                s += v
            if v == 10:
                last2 = True
                t = 0
            else:
                t += 1
        return s


if __name__ == "__main__":
    # player1 = [4,10,7,9]
    # player2 = [6,5,2,3]
    # player3 = [8,10,10,2]
    player1 = [9,7,10,7]
    player2 =[10,2,4,10]
    func = Solution().score
    print(func(player1))