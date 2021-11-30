from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        while True:
            for i, v in enumerate(tickets):
                if v > 0:
                    res += 1
                tickets[i] = v - 1
                if tickets[k] == 0:
                    return res


if __name__ == '__main__':
    tickets = [5, 1, 1, 1]
    k = 0
    # tickets = [2, 3, 2]
    # k = 2
    # tickets = [84, 49, 5, 24, 70, 77, 87, 8]
    # k = 3
    #  154
    func = Solution().timeRequiredToBuy
    print(func(tickets, k))
