
from typing import List
from bisect import bisect,bisect_left
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numbers_ls = []
        alphabet_ls = []
        alphabet_no_head_ls =[]
        for value in logs:
            vals = value.split(" ")
            if vals[1].isnumeric():
                numbers_ls.append(value)
            else:
                no_head = " ".join(vals[1:])
                ind = bisect(alphabet_no_head_ls,no_head)
                ind_left = bisect_left(alphabet_no_head_ls,no_head)
                if ind_left == ind:
                    alphabet_no_head_ls.insert(ind,no_head)
                    alphabet_ls.insert(ind,value)
                else:
                    for j,v in enumerate(alphabet_no_head_ls[ind_left:ind]):
                        if value > v:
                            alphabet_no_head_ls.insert(ind_left+j,no_head)
                            alphabet_ls.insert(ind_left,value)
                            pass
        alphabet_ls.extend(numbers_ls)
        return alphabet_ls

if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","g2 act car"]
    func = Solution().reorderLogFiles
    print(func(logs2))