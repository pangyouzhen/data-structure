from operator import le


class Solution:
    def minimizeResult(self, expression: str) -> str:
        ind = expression.index("+")
        left_index = ind
        right_index = ind
        res = "(" + expression + ')'
        init = eval(expression)
        for i in range(0,left_index):
            for j in range(right_index,len(expression)+1):
                left  = expression[:i] + '*(' + expression[i:ind]
                right = expression[ind+1:j] + ")*" + expression[j:len(expression)]
                exp = left + "+" + right
                # print(exp)
                # print("------")
                if exp.startswith("*"):
                    exp = exp[1:]
                if exp.endswith("*"):
                    exp = exp[:-1]
                try:
                    val = eval(exp)
                    if val < init:
                        res = exp
                        init =val
                except:
                    pass
            # res.replace("*")
        return res.replace("*","")
            


if __name__ == "__main__":
    func = Solution().minimizeResult
    expression = "5+22"
    print(func(expression))