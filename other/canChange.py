class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        d = {"_L":"L_","R_":"_R"}
        for i,v in d.items():
            if  i in start:
                self.canChange(start.replace(i, v), target)
        return False

if __name__ == "__main__":
    func = Solution().canChange
    start = "_L__R__R_"
    target = "L______RR"
    print(func(start, target))
