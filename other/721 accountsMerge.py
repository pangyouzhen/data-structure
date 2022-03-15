from typing import List


class Solution:
    # TODO
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        t = []
        for account in accounts:
            t.extend(account)