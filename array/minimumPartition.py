# TODO
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        slide_windows = []
        n = len(s)
        for i in range(n):
            while s[i] < k:
                slide_windows.append(s[i])
                if int("".join(slide_windows)) < k:
                    pass