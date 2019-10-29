import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        res = re.sub("/{2,}", "/", path)
        res_ls = res.split("/")
        filter_ls = list(filter(lambda x: x != ".", res_ls))
        result = ["/"]
        for v in filter_ls[1:]:
            if v == ".." and len(result) != 1:
                result.pop()
                result.pop()
            elif v != ".." and v:
                result.append(v)
                result.append("/")
        if result[-1] == "/" and len(result) != 1:
            result.pop()
        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    assert sol.simplifyPath('/a/./b/../../c/') == "/c"
    assert sol.simplifyPath("/../") == "/"
    assert sol.simplifyPath("/home//foo/") == "/home/foo"
    assert sol.simplifyPath("/a/../../b/../c//.//") == "/c"
    assert sol.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"