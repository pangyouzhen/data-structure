from typing import List
from collections import *
from base.tree.tree_node import TreeNode
from base.linked_list.ListNode import ListNode
from heapq import *
from functools import *
from bisect import *
from decimal import *

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x:x[0])
        if len(stockPrices) == 1:
            return 0
        if len(stockPrices) == 2:
            return 1
        res = 1
        pre = Decimal(stockPrices[1][1] - stockPrices[0][1])/Decimal(stockPrices[1][0] - stockPrices[0][0])
        for i in range(2,len(stockPrices)):
            val = Decimal(stockPrices[i][1] - stockPrices[i-1][1]) / Decimal(stockPrices[i][0] - stockPrices[i-1][0])
            if val == pre:
                continue
            else:
                pre = val 
                res += 1
        return res

if __name__ =="__main__":
    func = Solution().minimumLines
    nums =[]
    print(func(nums))