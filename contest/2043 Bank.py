from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.l: int = len(balance)
        self.balance: List[int] = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.l or account2 > self.l:
            return False
        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] = self.balance[account1 - 1] - money
            self.balance[account2 - 1] = self.balance[account2 - 1] + money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account > self.l:
            return False
        self.balance[account-1] = self.balance[account-1] + money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.l:
            return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] = self.balance[account - 1] - money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
