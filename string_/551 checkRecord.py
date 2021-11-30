from collections import Counter


class Solution:
    def checkRecord(self, s: str) -> bool:
        c = Counter(s)
        if "A" not in c.keys() or ("A" in c.keys() and c.get("A") < 2):
            if "LLL" not in s:
                return True
        return False

    def checkRecord2(self, s: str) -> bool:
        absents = lates = 0
        for i, v in enumerate(s):
            if v == "A":
                absents += 1
                if absents >= 2:
                    return False
            #  这里连续的判断
            if v == "L":
                lates += 1
                if lates >= 3:
                    return False
            else:
                lates = 0
        return True
