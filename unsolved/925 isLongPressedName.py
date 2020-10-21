class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        print("-------------------------------------")
        name_pointer = 0
        typed_pointer = 0
        # 两个索引必须都走完才行
        #  TODO ERROR
        while typed_pointer < len(typed):
            try:
                name_charter = name[name_pointer]
                typed_charter = typed[typed_pointer]
                print(f"{name_charter =}", f"{typed_charter = }")
                if typed_charter == name_charter:
                    typed_pointer += 1
                    name_pointer += 1
                else:
                    if name_pointer > 0 and typed_charter == name[name_pointer - 1]:
                        typed_pointer += 1
                    else:
                        return False
            except IndexError as e:
                name_pointer = len(name) - 1
        return True


if __name__ == '__main__':
    # name1 = "saeed"
    # typed1 = "ssaaedd"
    sol = Solution()
    # assert (sol.isLongPressedName(name1, typed1)) == False
    name2 = "vtkgn"
    typed2 = "vttkgnn"
    assert sol.isLongPressedName(name2, typed2) == True
    name3 = "pyplrz"
    typed3 = "ppyypllr"
    assert (sol.isLongPressedName(name3, typed3)) == False
    name4 = "alex"
    typed4 = "alexxr"
    assert sol.isLongPressedName(name4, typed4) == False
