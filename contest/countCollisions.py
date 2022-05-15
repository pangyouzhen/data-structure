from typing import List


class Solution:
    def countCollisions(self, directions: str) -> int:
        d = {
            "LL":[0,"L"],
            "LR":[0,"R"],
            "LS":[0,"S"],
            "RL":[2,"S"],
            "RR":[0,"R"],
            "RS":[1,"S"],
            "SL":[1,"S"],
            "SR":[0,"R"],
            "SS":[0,"S"]
        }
        res = 0
        a = []
        pre = directions[0]
        for i in range(1,len(directions)):
            new_state = pre + directions[i]
            res += d[new_state][0]
            pre = d[new_state][1]
            a.append(pre)
        print("".join(a))
        return res
            

if __name__ =="__main__":
    func = Solution().countCollisions
    nums ="SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
    # nums ="SSRSSRLLRSLL"
    print(func(nums))
