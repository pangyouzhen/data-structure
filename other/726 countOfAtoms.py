import re
import pysnooper


# TODO
class Solution:
    @pysnooper.snoop()
    def countOfAtoms(self, formula: str) -> str:
        if "(" not in formula:
            return
        new_formula = re.search("\((.*)\)", formula).group(1)
        self.countOfAtoms(new_formula)


if __name__ == '__main__':
    a = "K4(ON(SO3)2)2"
    sol = Solution()
    print(sol.countOfAtoms(a))
