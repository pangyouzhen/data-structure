class Solution:
    def simplifyPath(self, path: str) -> str:
        res = path.split("/")
        result = []
        for i in res:
            if i:
                if i == ".":
                    pass
                elif i == "..":
                    if len(result) >= 1:
                        del result[-1]
                else:
                    result.append(i)
        result.insert(0, "")
        ll = "/".join(result)
        if ll:
            return ll
        else:
            return "/"


if __name__ == '__main__':
    sol = Solution()
    # path = "/a/./b/../../c/"
    path = "/../"
    print(sol.simplifyPath(path))
