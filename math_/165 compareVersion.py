class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = [int(i) for i in version1.split(".")]
        version2_list = [int(i) for i in version2.split(".")]
        max_len = max(len(version1_list), len(version2_list))
        version1_list = version1_list + [0] * (max_len - len(version1_list))
        version2_list = version2_list + [0] * (max_len - len(version2_list))
        t = 0
        while t < max_len:
            if version1_list[t] > version2_list[t]:
                return 1
            elif version1_list[t] < version2_list[t]:
                return -1
            t = t + 1
        return 0


if __name__ == '__main__':
    sol = Solution()
    assert sol.compareVersion("0.1", "1.1") == -1
    assert sol.compareVersion("1.0.1", "1") == 1
    assert sol.compareVersion("7.5.2.4", "7.5.3") == -1
    assert sol.compareVersion("1.01", "1.001") == 0
    assert sol.compareVersion("1.0", "1.0.0") == 0
