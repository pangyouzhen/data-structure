from typing import List

from base.tree.tree_node import TreeNode

class Solution():
    def largestGoodInteger(self, num : str) -> str:
        res = ""
        pre = ""
        curr_num = 0
        for i,v in enumerate(num):
            if v != pre:
                curr_num = 1
                pre = v
            else:
                curr_num += 1
            if curr_num == 3:
                if res:
                    if int(pre) > int(res[0]):
                        res = pre
                else:
                    res = pre
        return res * 3
                

if __name__ =="__main__":
    func = Solution().largestGoodInteger
    nums ="677713333999"
    # root=TreeNode.from_strs(nums)
    print(func(nums))