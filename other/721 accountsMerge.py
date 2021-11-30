from typing import List


class Solution:
    # todo
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        t = []
        for account in accounts:
            t.extend(account)