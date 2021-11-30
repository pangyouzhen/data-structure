from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count_ = 0
        for i in items:
            if self.check_match(i, ruleKey, ruleValue):
                count_ += 1
        return count_

    def check_match(self, item: List[str], ruleKey: str, ruleValue):
        if ruleKey == "type":
            if item[0] == ruleValue:
                return True
        elif ruleKey == "color":
            if item[1] == ruleValue:
                return True
        elif ruleKey == "name":
            if item[2] == ruleValue:
                return True


if __name__ == '__main__':
    items = [["phone", "blue", "pixel"],
             ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    sol = Solution()
    print(sol.countMatches(items, ruleKey, ruleValue))
