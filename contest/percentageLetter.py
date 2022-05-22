from typing import List
from collections import *
from base.tree.tree_node import TreeNode
from base.linked_list.ListNode import ListNode
from heapq import *
from functools import *
from bisect import *

class Solution:
    def percentageLetter(self, s:str,letter:str) -> int:
        t = s.count(letter)
        return int(t/len(s) * 100 )

if __name__ =="__main__":
    func = Solution().percentageLetter
    nums =[]
    print(func(nums))