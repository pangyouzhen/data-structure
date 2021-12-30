from typing import List
from collections import Counter


class Solution():
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        group = l / groupSize
        if int(group) != group:
            return False
        c_dic = Counter(hand)
        init_min_val = min(c_dic.keys())
        for i in range(int(group)):
            for j in range(groupSize):
                k = init_min_val + j
                if k in c_dic and c_dic[k] > 0:
                    c_dic[k] -= 1
                    if c_dic[k] == 0:
                        del c_dic[k]
                else:
                    return False
            if c_dic:
                init_min_val = min(c_dic.keys())
        return True


if __name__ == "__main__":
    func = Solution().isNStraightHand
    hands = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    group_size = 3
    print(func(hands, group_size))
