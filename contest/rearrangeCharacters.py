from typing import List
from collections import *
from base.tree.tree_node import TreeNode
from base.linked_list.ListNode import ListNode
from heapq import *
from functools import *
from bisect import *

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(s)
        t = Counter(target)
        min_val =float('inf')
        for i in t.keys():
            if i not in c.keys():
                return 0
            else:
                 temp = int(c[i] / t[i])
                 if temp < min_val:
                     min_val = temp
        return min_val

if __name__ =="__main__":
    func = Solution().rearrangeCharacters
    s = "abc"
    target = "abcd"
    print(func(s,target))