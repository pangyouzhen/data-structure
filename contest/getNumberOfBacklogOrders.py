import bisect


class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        buy_backlog = []
        buy_backlog_amount = []
        # 维护一个有序列表，buy 是从大到小
        sell_backlog = []
        sell_backlog_amount = []
        # 维护一个有序列表，buy 是从小到大
        for i in orders:
            pricei, amount, orderType = i
            if orderType == 0:
                while sell_backlog and pricei >= sell_backlog[-1] and amount > 0:
                    sell_backlog_amount[-1] -= 1
                    if sell_backlog_amount[-1] == 0:
                        sell_backlog_amount.pop()
                        sell_backlog.pop()
                    amount -= 1
                if amount > 0:
                    bisect.insort(buy_backlog, pricei)
                    position = buy_backlog.index(pricei)
                    buy_backlog_amount.insert(position, amount)
            if orderType == 1:
                while buy_backlog and pricei <= buy_backlog[-1] and amount > 0:
                    buy_backlog_amount[-1] -= 1
                    if buy_backlog_amount[-1] == 0:
                        buy_backlog_amount.pop()
                        buy_backlog.pop()
                    amount -= 1
                if amount > 0:
                    bisect.insort(sell_backlog, pricei)
                    position = sell_backlog.index(pricei)
                    sell_backlog_amount.insert(position, amount)
        print(buy_backlog)
        print(buy_backlog_amount)
        print(sell_backlog)
        print(sell_backlog_amount)
        a = sum(buy_backlog_amount) + sum(sell_backlog_amount)
        return a % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    # orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
    # orders = [[10, 5, 0], [15, 2, 1]]
    # orders = [[7, 1000000000, 1], [15, 3, 0]]
    orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
    print(sol.getNumberOfBacklogOrders(orders))
