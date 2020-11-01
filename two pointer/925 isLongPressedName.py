#  这个虽然是双指针，但是边界问题总是出错
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        last_charter = name[0]
        return self.isLongPressedName_last_charter(name, typed, last_charter)

    def isLongPressedName_last_charter(self, name, typed, last_charter):
        if len(name) == len(typed) == 0:
            return True
        if len(name) > len(typed):
            return False
        if len(name) > 0 and typed[0] == name[0]:
            last_charter = name[0]
            return self.isLongPressedName_last_charter(name[1:], typed[1:], last_charter)
        elif typed[0] == last_charter:
            return self.isLongPressedName_last_charter(name, typed[1:], last_charter)
        else:
            return False


if __name__ == '__main__':
    name1 = "saeed"
    typed1 = "ssaaedd"
    sol = Solution()
    assert (sol.isLongPressedName(name1, typed1)) == False
    name2 = "vtkgn"
    typed2 = "vttkgnn"
    assert sol.isLongPressedName(name2, typed2) == True
    name3 = "pyplrz"
    typed3 = "ppyypllr"
    assert (sol.isLongPressedName(name3, typed3)) == False
    name4 = "alex"
    typed4 = "alexxr"
    assert sol.isLongPressedName(name4, typed4) == False
