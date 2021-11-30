from typing import List
from pysnooper import snoop
from functools import lru_cache


# 这个可以抽象成一个线性规划的问题，线性规划和动态规划不是同一维度上，不能比较，动态规划只是一种思想
# 但是动态规划用了数学归纳法，每个的状态涉及到上面和一个状态，所以和线性规划是完全不同的,
# 这里可以看成一棵树，然后进行剪枝


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # 过滤不需要计算的大礼包，只保留需要计算的大礼包
        filter_special = []
        for sp in special:
            if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
                filter_special.append(sp)

        # 记忆化搜索计算满足购物清单所需花费的最低价格
        @lru_cache(None)
        @snoop()
        def dfs(cur_needs):
            # 不购买任何大礼包，原价购买购物清单中的所有物品
            min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
            for cur_special in filter_special:
                special_price = cur_special[-1]
                nxt_needs = []
                for i in range(n):
                    if cur_special[i] > cur_needs[i]:  # 不能购买超出购物清单指定数量的物品
                        break
                    nxt_needs.append(cur_needs[i] - cur_special[i])
                if len(nxt_needs) == n:  # 大礼包可以购买
                    min_price = min(min_price, dfs(tuple(nxt_needs)) + special_price)
            return min_price

        return dfs(tuple(needs))


if __name__ == '__main__':
    price = [2, 5]
    special = [[3, 0, 5],
               [1, 2, 10]]
    needs = [3, 2]
    func = Solution().shoppingOffers
    print(func(price, special, needs))
