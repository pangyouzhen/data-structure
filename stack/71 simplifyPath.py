import os


class Solution:
    def simplifyPath(self, path: str) -> str:
        # python 内置函数 解决方案
        # return os.path.realpath(path)
        # 栈解决方案
        names = path.split("/")
        stack = []
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/"+"/".join(name)


if __name__ == '__main__':
    sol = Solution()
    #path = "/a/./b/../../c/"
    path = "/a/../../b/../c//.//"
    # path = "/../"
    # path = "/home//path"
    print(sol.simplifyPath(path))
