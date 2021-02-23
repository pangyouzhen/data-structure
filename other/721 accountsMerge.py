from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        t = []
        for account in accounts:
            t.extend(account)