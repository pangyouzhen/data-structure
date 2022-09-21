from copy import deepcopy
from typing import List


class ATM:

    def __init__(self):
        self.c = [0, 0, 0, 0, 0]
        self.v = [20, 50, 100, 200, 500]
        self.reverse_v = self.v[::-1]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount):
            self.c[i] += v

    def withdraw(self, amount: int) -> List[int]:
        result = [0, 0, 0, 0, 0]
        t = deepcopy(self.c)
        while amount > 0:
            for i, v in enumerate(self.reverse_v):
                l = int(amount / v)
                ct = min(self.c[4 - i], l)
                amount -= ct * v
                t[4 - i] -= l
                result[4 - i] += l
            if i == 4:
                break
        if amount != 0:
            return [-1]
        else:
            self.c = t
            return result


if __name__ == "__main__":
    atm = ATM()
    # atm.deposit([0,0,1,2,1])
    # print(atm.c)
    # atm.withdraw(600)
    # print(atm.c)
    # atm.deposit([0,1,0,1,1]); 
    # print(atm.c)                # // 机器中剩余钞票数量为 [0,1,0,3,1] 。
    # atm.withdraw(600); 
    # print(atm.c)      
    # #  返回 [-1] 。机器会尝试取出 $500 的钞票，然后无法得到剩余的 $100 ，所以取款请求会被拒绝。
    # # 由于请求被拒绝，机器中钞票的数量不会发生改变。
    # atm.withdraw(550);  
    # print(atm.c)
    ["ATM", "deposit", "withdraw"]
    [[], [[0, 10, 0, 3, 0]], [500]]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
