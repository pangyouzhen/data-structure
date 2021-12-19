from typing import List

class Solution():
    def addSpaces2(self, s: List[str],spaces:List[int]) -> str:
        res = ""
        for i,v in enumerate(s):
            if i in spaces:
                res += " "
            res += v
        return res
    def addSpaces(self, s: List[str],spaces:List[int]) -> str:
        l = len(s)
        res = []
        spaces.insert(0,0)
        spaces.append(l)
        for j in range(1,len(spaces)):
            if spaces[j] == 0:
                res.append(" ")
                continue
            n = s[spaces[j-1]:spaces[j]]
            res.append(n)
        return " ".join(res)
            
           

if __name__ =="__main__":
    func = Solution().addSpaces
    s = "LeetcodeHelpsMeLearn"
    spaces = [8,13,15]
    print(func(s,spaces))