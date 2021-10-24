from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """
        这个可以抽象成一个线性规划的问题，线性规划和动态规划不是同一维度上，不能比较，动态规划只是一种思想
        但是动态规划用了数学归纳法，每个的状态涉及到上面和一个状态，所以和线性规划是完全不同的
        """
        # 先排除大于总数的大礼包
        special_remains = []
        for s in special:
            a = True
            for i, v in zip(s, needs):
                if i > v:
                    a = False
                    break
            if a:
                special_remains.append(s)


if __name__ == '__main__':
    func = Solution().shoppingOffers
