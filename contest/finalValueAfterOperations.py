from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        init = 0
        for i in operations:
            if i in ["++X", "X++"]:
                init += 1
            else:
                init -= 1
        return init
